import paho.mqtt.client as mqtt
import pandas as pd

data=[]
client=mqtt.Client()

client.connect('broker.hivemq.com',1883)
print('Broker Connected')

client.subscribe('gpcet/data')

i=0
def notification(client,userdata,msg):
    global i
    k=msg.payload
    k=k.decode('utf-8')
    k=k.split(':')
    h=k[1]
    t=k[-1]
    h=h.split(',')[0]
    t=t[:-1]
    # print(h)
    # print(t)
    dummy=[]
    dummy.append(h)
    dummy.append(t)
    # print(dummy)
    data.append(dummy)
    print(data)
    i+=1
    if i==10:
        df=pd.DataFrame(data)
        df.to_csv('data.csv')
        i=0

client.on_message=notification
client.loop_forever()
