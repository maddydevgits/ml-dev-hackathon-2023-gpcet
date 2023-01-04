import paho.mqtt.client as mqtt
from random import randint
import time

client=mqtt.Client()

client.connect('broker.hivemq.com',1883)
print('Broker Connected')

while True:
    k="{'Humidity':"+str(randint(20,100))
    k+=",'Temperature':"+str(randint(20,30))
    k+="}"
    print(k)
    client.publish('gpcet/data',k)
    time.sleep(4)
