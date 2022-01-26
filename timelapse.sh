#l/bin/bash
DATE=$(date +"%d-%m-%Y_%H")
python3 /home/pi/Pictures/timelapse/on.py
libcamera-jpeg -o /home/pi/Pictures/timelapse/$DATE.jpg
python3 /home/pi/Pictures/timelapse/off.py
