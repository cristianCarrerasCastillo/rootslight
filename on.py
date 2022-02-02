import RPi.GPIO as GPIO
from datetime import datetime

now = datetime.now()
mensaje = str(now)
log = open('/home/pi/Pictures/timelapse/log.log','a')

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT,initial=GPIO.LOW)
GPIO.output(4, GPIO.HIGH)
mensaje += ' - se ejecuto on.py\n'
log.write(mensaje)
log.close()
