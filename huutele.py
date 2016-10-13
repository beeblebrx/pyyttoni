#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

sense = SenseHat()
client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
  temp = sense.get_temperature()
  humidity = sense.get_humidity()
  pressure = sense.get_pressure()
  temp_from_hum = sense.get_temperature_from_humidity()
  temp_from_press = sense.get_temperature_from_pressure()
  client.publish("robot/senses/temperature", temp)
  client.publish("robot/senses/humidity/humidity", humidity)
  client.publish("robot/senses/humidity/temperature", temp_from_hum)
  client.publish("robot/senses/pressure/pressure", pressure)
  client.publish("robot/senses/pressure/temperature", temp_from_press)
  time.sleep(1)

client.disconnect()


  


