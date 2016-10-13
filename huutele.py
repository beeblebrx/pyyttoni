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
  client.publish("topic/senses", "t:{0},h:{1},p:{2}".format(temp, humidity, pressure))
  time.sleep(1)

client.disconnect()


  


