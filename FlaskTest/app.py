#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from PIL import Image

#Initialize the Flask app
app = Flask(__name__)
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



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)