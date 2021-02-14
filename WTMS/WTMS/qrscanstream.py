#Import necessary libraries
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

#Initialize the Flask app
camera = cv2.VideoCapture(0)
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                if len(str(obj.data))>0:
                    f = open("scandata.txt", "w")
                    f.write(str(obj.data))
                    f.close()
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result