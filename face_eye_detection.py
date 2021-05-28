import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        my_f = gray[y:y+h, x:x+w]
        my_fincol = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(my_f, 1.3, 5)
        for (x_e, y_e, w_e, h_e) in eyes:
            cv2.circle(my_fincol, (x_e+w_e//2, y_e+h_e//2), 5, (0, 255, 0), 5)

    cv2.imshow("cam", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
sys.exit()
