#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import data_manage as dm

# This is the Subscriber

conn = dm.create_connection(r"attendance.db")

count = 0

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/register")

def on_message(client, userdata, msg):
  print("Received Message...")
  #print(str(count))
  print(msg.payload.decode())

  word = msg.payload.decode()
  print(type(word))
  attributes = word.split('|')
  print(attributes)

  # identity = (attributes[i] for i in range(0, len(attributes)))

  print(tuple(attributes))
  dm.insert_attendance(conn, tuple(attributes))

  count = count + 1

#  if msg.payload.decode() == "Hello world!":
#    print("Yes!")
#    client.disconnect()
    
client = mqtt.Client()
client.connect("192.168.1.3",1883,600)

client.on_connect = on_connect
client.on_message = on_message

try:
	client.loop_forever()
# Catches SigINT
except KeyboardInterrupt:
	client.disconnect()