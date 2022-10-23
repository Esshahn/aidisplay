#!/bin/bash
# slideshow script for raspberry pi
# this file is for autolaunching your slideshow program fbi at startup
#

echo "restarting fbi"
killall fbi
fbi -noverbose -a /home/pi/code/aidisplay/images/*.png
