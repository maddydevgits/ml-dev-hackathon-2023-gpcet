import paho.mqtt.client as mqtt

# create client object
client=mqtt.Client()

client.connect('broker.hivemq.com',1883)
print('Broker Connected')

topic='gpcet/ml'
client.subscribe(topic)

def notification(client,userdata,msg):
    print(msg.payload)

client.on_message=notification
client.loop_forever()
