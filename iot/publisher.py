import paho.mqtt.client as mqtt
import time
import random
import json

broker = "localhost"
client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    data = {
        "trafic": random.randint(10, 100),
        "temperature": round(random.uniform(20, 35), 2)
    }

    client.publish("aiot/data", json.dumps(data))
    print("Données envoyées :", data)

    time.sleep(2)