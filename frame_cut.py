# -*- coding: utf-8 -*-
"""
Simple script to take every nth frame out of a video as a jpeg
Tosses out blurry images

Author:
@ Kalkberg

Requires:
    OpenCV
"""
import cv2

video = "Trench.mp4"
n = 47
blurthresh = 100 # Threshold for determining if image is blurry, adjust as needed
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
        
        # Check if imaage is blurry, if not, write
        if cv2.Laplacian(frame, cv2.CV_64F).var() > blurthresh:
        
            cv2.imwrite(video[:-4] + "frame%d.jpg" % count, frame)
