#!/usr/bin/env python3
import time, json, random
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "sensors/joystick"
client = mqtt.Client("joystick-pub")
client.connect(broker, port, 60)

try:
    while True:
        payload = {"x": random.randint(-100,100), "y": random.randint(-100,100), "ts": int(time.time())}
        client.publish(topic, json.dumps(payload), qos=1)
        print("published joystick:", payload)
        time.sleep(0.5)
except KeyboardInterrupt:
    client.disconnect()
