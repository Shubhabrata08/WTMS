from django.shortcuts import render
import os
from pathlib import Path
from django.http import StreamingHttpResponse
# Create your views here.
#Import necessary libraries

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

#Initialize the Flask app


def gen_frames():  
    camera = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            camera.release()
            break
        else:
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                if len(str(obj.data))>0:
                    cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
                    f = open("scandata.txt", "w")
                    f.write(str(obj.data))
                    f.close()
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
   

def home(request):
    return render(request,'home.html')
def issue(request):
    #exec(open(os.path.join(Path(__file__).resolve().parent.parent,'WTMS\\qrscan.py')).read()) 
    return StreamingHttpResponse(gen_frames(),content_type='multipart/x-mixed-replace; boundary=frame')
