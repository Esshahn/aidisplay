#!/bin/bash
# slideshow script for raspberry pi
# this file is for autolaunching your slideshow program fbi at startup
#

echo "starting fim"
fim --slideshow 5 -noverbose -a /home/pi/code/aidisplay/images/*.png
