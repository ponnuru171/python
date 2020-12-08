import picamera
print("image program")
with picamera.PiCamera() as camera:
    camera.resolutin=(2592,1944)
    camera.capture("/home/pi/image.jpg")
print("photo is saved in /home/pi")