import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


screen_width, screen_height = pyautogui.size()


cap = cv2.VideoCapture(0)


click_threshold = 40 

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            landmarks = hand_landmarks.landmark
            index_x = int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
            index_y = int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)
            thumb_x = int(landmarks[mp_hands.HandLandmark.THUMB_TIP].x * w)
            thumb_y = int(landmarks[mp_hands.HandLandmark.THUMB_TIP].y * h)

            
            mouse_x = screen_width * index_x // w
            mouse_y = screen_height * index_y // h
            pyautogui.moveTo(mouse_x, mouse_y)

            
            distance = ((thumb_x - index_x)**2 + (thumb_y - index_y)**2)**0.5


            
            if distance < click_threshold:
                pyautogui.click()

    
    cv2.imshow("AI Virtual Mouse", frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()