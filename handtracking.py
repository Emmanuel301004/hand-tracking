import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
        # Get palm center (landmark 9)
        hand1 = results.multi_hand_landmarks[0].landmark[9]
        hand2 = results.multi_hand_landmarks[1].landmark[9]

        h, w, _ = frame.shape
        x1, y1 = int(hand1.x * w), int(hand1.y * h)
        x2, y2 = int(hand2.x * w), int(hand2.y * h)

        # Distance between two palms
        dist = math.hypot(x2 - x1, y2 - y1)

        if dist < 200:  # threshold (adjust if needed)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            # Draw glowing Rasengan ball
            cv2.circle(frame, (cx, cy), 60, (255, 0, 0), -1)   # solid blue
            cv2.circle(frame, (cx, cy), 90, (215, 200, 0), 4)  # glowing ring
            cv2.putText(frame, "Emmanuel s02 RASENGAN!!!", (cx - 80, cy - 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        # Draw both hands normally
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Rasengan Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
