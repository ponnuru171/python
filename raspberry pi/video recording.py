import picamera
from time import sleep
print("start recording")
with picamera.PiCamera() as camera:
    camera.start_recording("myvideo.h264")
    sleep(10)
    camera.stop_recording()
print("recording completed")