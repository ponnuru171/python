import picamera
import time
from time import sleep
a=int(input("enter no.of recordings "))
with picamera.PiCamera() as camera:
    for i in range(1,a+1):
        ts=(time.strftime("%Y %d %b %H.%M.%S"))
        sai=ts + "video.h264"
        print("video",i,"start recording")
        camera.start_recording(sai)
        sleep(5)
        camera.stop_recording()
        print("video",i,"is completed")
        sleep(5)
    print("all",a, "recordings completed")