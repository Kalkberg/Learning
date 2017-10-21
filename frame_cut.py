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
    
    # Count frame number
    count += 1
    
    # If frame number divisible by n, save it as a jpg
    if count % n == 0:
        cv2.imwrite(video[:-4] + "_frame%d.jpg" % count, frame) 
    
    # Break when video is over
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break