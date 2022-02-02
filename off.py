import RPi.GPIO as GPIO
from datetime import datetime

now = datetime.now()
mensaje = str(now)
log = open('/home/pi/Pictures/timelapse/log.log','a')

#Definimos el modo BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Ahora definimos el pin GPIO 17 como salida
GPIO.setup(4, GPIO.OUT,initial=GPIO.LOW)
#Y le damos un valor logico bajo para apagar el LED
GPIO.output(4, GPIO.LOW)
#Finalmente liberamos todos los pines GPIO, es decir, los desconfiguramos)
GPIO.cleanup()

mensaje += ' - se ejecuto off.py\n'
log.write(mensaje)
log.close()
