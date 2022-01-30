import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(4, GPIO.HIGH)
