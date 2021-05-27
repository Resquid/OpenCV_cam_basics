import numpy as np
import cv2

# kamerka
cap = cv2.VideoCapture(0)

while True:
    # ret - sprawdzenie czy dziala, frame - klatka z kamerki
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # linia, kwadrat, koło, tekst, zmiana koloru
    # img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # img = cv2.line(img, (width, 0), (0, height), (0, 255, 0), 10)
    # img = cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), 10)
    # img = cv2.circle(img, (width // 2, height // 2), 100, (128, 128, 128), -1)
    # font = cv2.FONT_HERSHEY_DUPLEX
    # img = cv2.putText(img, "CZE", (width // 2, height // 2), font, 4, (0, 0, 0), 5, cv2.LINE_AA)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # wykrycie rogów
    corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.1, 10)
    corners = np.int0(corners)

    # rysowanie kół jako rogów
    for corner in corners:
        # ravel = flatten
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    # łączenie kół
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            cv2.line(frame, corner1, corner2, (255, 0, 0), 1)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
