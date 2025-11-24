import random
import time
import paho.mqtt.client as mqtt

THE_BROKER = "mosquitto"
THE_TOPIC_X = "gateway/joystick X"
THE_TOPIC_Y = "gateway/joystick Y"
THE_TOPIC_BUTTON = "gateway/button"
THE_PORT = 1883

mqttc = mqtt.Client()
mqttc.connect(THE_BROKER, THE_PORT)

while True:
    # Gebruik bereik -100 tot 100!
    x_value = random.randint(-100, 100)
    y_value = random.randint(-100, 100)
    button_value = random.randint(0, 1)

    mqttc.publish(THE_TOPIC_X, str(x_value))
    mqttc.publish(THE_TOPIC_Y, str(y_value))
    mqttc.publish(THE_TOPIC_BUTTON, str(button_value))

    print(f"Publishing: X={x_value}, Y={y_value}, Button={button_value}")
    time.sleep(2)