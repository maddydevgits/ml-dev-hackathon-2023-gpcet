import paho.mqtt.client as mqtt

# create client object
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

topic='gpcet/ml'
msg='hi madhu here'

client.publish(topic,msg)
