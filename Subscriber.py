import paho.mqtt.client as mqtt
import time
from validKey import validKey

key = ''
pastKey = ''
attackFlag = False

def on_message(client, userdata, message):
    if(message.topic == "KEY2"):
        payload = str(message.payload.decode("utf-8"))
        if validKey(payload):
            global key
            global pastKey
            pastKey = key
            key = payload
        else:
            return
    else:
        msg = message.payload.decode("utf-8")
        last10 = (msg[len(msg)-10:len(message.payload)])
        if key == last10 or pastKey == last10:
            print("received message: " ,str(message.payload.decode("utf-8")))
        else:
            return

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("DOORBELL2-PUB")  # Subscribe to the topic “digitest/test1”, receive any messages published on it
    client.subscribe("KEY2")

client = mqtt.Client("DOORBELL1-SUB")

client.on_connect=on_connect
client.on_message=on_message 

client.connect("mqtt.eclipseprojects.io", keepalive=60) 
client.loop_forever()


    