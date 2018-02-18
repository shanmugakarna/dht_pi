#!/usr/bin/python
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
pin_in = 17
pin_out = 27
GPIO.setup(pin_out, GPIO.OUT)

def read(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = temperature * 9/5.0 + 32
    return humidity, temperature

try:
    while True:
        humidity, temperature = read(sensor, pin_in)
        print 'Temperature : {0:0.1f}*  Humidity : {1:0.1f}%'.format(
            temperature, humidity)
        if temperature > 88.5:
            print "Tempeature above set limit, switching OFF relay"
            GPIO.output(pin_out, 1)
        else:
            print "Tempeature below set limit, switching ON relay"
            GPIO.output(pin_out, 0)
        time.sleep(5)
except KeyboardInterrupt:
    print "Interrupted."
finally:
    print "Cleaning Up"
    GPIO.cleanup()
