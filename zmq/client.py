from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ip = '192.168.1.143'
print('d')
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(ip))



rpiName = socket.gethostname()
#vs = VideoStream(usePiCamera=True).start()
#vs = VideoStream(src=0).start()
cap = cv2.VideoCapture(0)
time.sleep(2.0)
i = 0
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(1024))
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(768))

while True:
    #read the frame from the camera and send it to the server
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #i+=1
    sender.send_image(rpiName, frame)
    #print(i)
        



