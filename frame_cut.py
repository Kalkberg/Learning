# -*- coding: utf-8 -*-
"""
Simple script to take every nth frame out of a video as a jpeg

Author:
@ Kalkberg

"""
import cv2

video = "cup.mp4"
n = 30

vidcap = cv2.VideoCapture(video)

# count number of frames in video
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

# Set counter to zero
count = 0

while count < length:
    # Capture frame-by-frame
    ret, frame = vidcap.read()
    
    # Count frame number
    count += 1
    
    # If frame number divisible by n, save it as a jpg
    if count % n == 0:
        cv2.imwrite(video[:-4] + "_frame%d.jpg" % count, frame)