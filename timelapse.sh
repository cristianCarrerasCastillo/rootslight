#l/bin/bash
# Dev: Cristian Carreras
DATE=$(date +"%d-%m-%Y_%H")
echo 2 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio2/direction
echo 1 > /sys/class/gpio/gpio2/value
libcamera-jpeg -o /home/pi/Pictures/timelapse/$DATE.jpg
echo 0 > /sys/class/gpio/gpio2/value 
