# -*- coding: utf-8 -*-
"""
Simple script to take every nth frame out of a video as a jpeg

Author:
@ Kalkberg

"""
import cv2

video = "testvid.mp4"
n = 150

vidcap = cv2.VideoCapture(video)

# Set counter to zero
count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = vidcap.read()
    
    count += 1

    if count % n == 0:
        cv2.imwrite(video[:-4] + "frame%d.jpg" % count, frame) 
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break