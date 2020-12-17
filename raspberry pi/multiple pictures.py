import picamera
import time
from time import sleep
print("image programm")
a=int(input("enter no.of photos"))
with picamera.PiCamera() as camera:
    for i in range(0,a):
        camera.resolution = (2592,1944)
        ts=(time.strftime("%Y %d %b %H.%M.%S"))
        sai= ts + "image.jpg"
        camera.capture(sai)
        print("picture",i,"is taken")
        sleep(5)
    print("photo taken")