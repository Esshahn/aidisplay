#!/bin/bash
python3 /home/pi/Code/aidisplay/get-weather.py && \
python3 /home/pi/Code/aidisplay/generate-prompt.py && \
python3 /home/pi/Code/aidisplay/generate-image.py