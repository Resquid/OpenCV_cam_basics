import cv2
import sys
import time

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
hand_cascade = cv2.CascadeClassifier("hand_cascade.xml")
closed_eyes_cascade = cv2.CascadeClassifier("closed_eye_cascade.xml")
Timer = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 6)
    closed_eyes = closed_eyes_cascade.detectMultiScale(gray, 1.3, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, 'Head', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
        my_f = gray[y:y+h, x:x+w]
        my_fincol = frame[y:y+h, x:x+w]

    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, 'Hand', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

    for (x_e, y_e, w_e, h_e) in closed_eyes:
        cv2.rectangle(frame, (x_e, y_e), (x_e + w_e, y_e + h_e), (255, 0, 0), 3)
        cv2.putText(frame, 'Opened eye', (x_e, y_e), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

    if len(closed_eyes) == 0 and not Timer:
        t0 = time.time()
        Timer = True
    elif len(closed_eyes) >= 1:
        t0 = 0
        Timer = False
    if time.time() - t0 >= 3 and Timer:
        print("Sleeping")
    else:
        print("Not sleeping")





    cv2.imshow("cam", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
sys.exit()
