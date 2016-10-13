#!/usr/bin/env python

import sys
import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

broker_url = sys.argv[1] if (len(sys.argv) > 1) else 'localhost'
broker_port = int(sys.argv[2]) if (len(sys.argv) > 2) else 1883

sense = SenseHat()
client = mqtt.Client()
client.connect(broker_url, broker_port, 60)

while True:
  temp = sense.get_temperature()
  humidity = sense.get_humidity()
  pressure = sense.get_pressure()
  temp_from_hum = sense.get_temperature_from_humidity()
  temp_from_press = sense.get_temperature_from_pressure()
  orientation = sense.get_orientation_degrees()
  compass = sense.get_compass()
  gyro = sense.get_gyroscope()
  accelerometer = sense.get_accelerometer()

  client.publish("robot/senses/temperature", temp)
  client.publish("robot/senses/humidity/humidity", humidity)
  client.publish("robot/senses/humidity/temperature", temp_from_hum)
  client.publish("robot/senses/pressure/pressure", pressure)
  client.publish("robot/senses/pressure/temperature", temp_from_press)
  client.publish("robot/senses/orientation/pitch", orientation["pitch"])
  client.publish("robot/senses/orientation/roll", orientation["roll"])
  client.publish("robot/senses/orientation/yaw", orientation["yaw"])
  client.publish("robot/senses/compass", compass)
  client.publish("robot/senses/gyroscope/pitch", gyro["pitch"])
  client.publish("robot/senses/gyroscope/roll", gyro["roll"])
  client.publish("robot/senses/gyroscope/yaw", gyro["yaw"])
  client.publish("robot/senses/accelerometer/pitch", accelerometer["pitch"])
  client.publish("robot/senses/accelerometer/roll", accelerometer["roll"])
  client.publish("robot/senses/accelerometer/yaw", accelerometer["yaw"])
  time.sleep(1)

client.disconnect()
