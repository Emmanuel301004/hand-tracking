import cv2
import mediapipe as mp
import numpy as np
import math
import sys

# For Windows volume control
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    volume_control = True
except ImportError:
    print("⚠️ Pycaw not installed. Run: pip install pycaw comtypes")
    volume_control = False

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Could not access camera.")
        sys.exit(1)

    hands = mp_hands.Hands(min_detection_confidence=0.7,
                           min_tracking_confidence=0.7)

    # Setup Windows volume control
    if volume_control:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        vol_range = volume.GetVolumeRange()
        min_vol, max_vol = vol_range[0], vol_range[1]

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Frame not captured, skipping...")
                continue

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    h, w, _ = frame.shape
                    # Thumb tip (4), Index tip (8)
                    x1, y1 = int(hand.landmark[4].x * w), int(hand.landmark[4].y * h)
                    x2, y2 = int(hand.landmark[8].x * w), int(hand.landmark[8].y * h)

                    # Draw circles
                    cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
                    cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

                    # Distance between fingers
                    dist = math.hypot(x2 - x1, y2 - y1)

                    if volume_control:
                        # Map distance (20–200) to volume range
                        vol = np.interp(dist, [20, 200], [min_vol, max_vol])
                        volume.SetMasterVolumeLevel(vol, None)
                        vol_percent = np.interp(dist, [20, 200], [0, 100])
                        cv2.putText(frame, f'Volume: {int(vol_percent)}%', (50, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

                    mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Hand Volume Control", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
