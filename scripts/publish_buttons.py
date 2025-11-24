#!/usr/bin/env python3
import time, json, random
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "sensors/buttons"
client = mqtt.Client("buttons-pub")
client.connect(broker, port, 60)

try:
    while True:
        payload = {"btn1": random.choice([0,1]), "btn2": random.choice([0,1]), "ts": int(time.time())}
        client.publish(topic, json.dumps(payload), qos=1)
        print("published buttons:", payload)
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
