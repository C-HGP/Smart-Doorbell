import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))

    client.subscribe("bell")

def on_message(client, userdata, msg):

    print(msg.topic+" "+str(msg.payload))
    os.system("curl -X POST -H \'Content-type: application/json\' --data \'{\"text\":\"Someone is at the door... <http://192.168.10.71:8080/stream.html|Click here for video feed>\"}\' YOURWEBHOOKURLHERE")
    os.system("play BingBong.mp3 vol 9")

client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message


client.connect("192.168.10.71")

client.loop_forever()
