#!usr/bin/env/ python
#apaga.py
#importamos la libreria GPIO
import RPi.GPIO as GPIO
#Definimos el modo BCM
GPIO.setmode(GPIO.BCM)
#Ahora definimos el pin GPIO 17 como salida
GPIO.setup(4, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
#Y le damos un valor logico bajo para apagar el LED
GPIO.output(4, GPIO.LOW)
#Finalmente liberamos todos los pines GPIO, es decir, los desconfiguramos)
GPIO.cleanup()
