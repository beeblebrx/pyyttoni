#!/usr/bin/env python

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Yhteys auki " + str(rc))
  client.subscribe("robot/senses/#")

def on_message(client, userdata, msg):
  print(msg.topic)
  print(msg.payload)
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

