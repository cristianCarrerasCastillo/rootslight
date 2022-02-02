#l/bin/bash
DATE=$(date +"%d-%m-%Y_%H")
echo "$DATE - inicio ejecución .sh">>/home/pi/Pictures/timelapse/log.log
python3 /home/pi/Pictures/timelapse/on.py

libcamera-jpeg -o /home/pi/Pictures/timelapse/$DATE.jpg
echo "$DATE Se Saco la foto">>/home/pi/Pictures/timelapse/log.log
python3 /home/pi/Pictures/timelapse/off.py

