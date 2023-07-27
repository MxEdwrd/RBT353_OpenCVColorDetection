import cv2
import numpy as np

from PIL import Image

from util import get_limits

blue = [255, 0, 0]

cap = cv2.VideoCapture(1)

while True: 
    ret, frame = cap.read()

    frame=cv2.resize(frame,(640,480))

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=blue)

    mask = cv2.inRange(hsv, lowerLimit, upperLimit)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
