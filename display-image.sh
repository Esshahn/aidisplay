#!/bin/bash
# slideshow script for raspberry pi
# this file is for autolaunching your slideshow program fbi at startup
#
INTERVAL=5 #how many seconds for each slide
fbi -noverbose -a -t $INTERVAL /home/pi/code/aidisplay/images/*.png
