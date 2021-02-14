import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
flag=0
while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
        if len(str(obj.data))>0:
            f = open("scandata.txt", "w")
            f.write(str(obj.data))
            f.close()
            flag=1

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if flag==1:
        cap.release()
        cv2.destroyAllWindows()
        break