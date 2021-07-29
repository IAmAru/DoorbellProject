import paho.mqtt.client as mqtt
import keyboard
import os
import string
import time
import random

i = 0
temp = ['']

for i in range(3):
    try:
        f = open(f"{os.getcwd()}/Messages/message{i}.txt", 'r')
        temp.append(f.read())
        f.close()
    except (FileNotFoundError, IOError):
        print(f"File 'message{i}' not found. Please make sure there is a /Messages folder in the root directory and run setup.py") 
        exit()

if(temp[1] == '' or temp[2] == '' or temp[3] == ''):
    print("Messages are not set up correctly. Please run the setup.py file.")
    exit()

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("DOORBELL1-PUB")
client.connect(mqttBroker)

while True:
    time.sleep(0.2)
    keypress = keyboard.is_pressed("e")
    while ~keypress:
        #This creates a random string of 10 characters. A valid password looks like: AlaBcDeFgHiJ
        key = (''.join(random.choice(string.ascii_letters) for i in range(10)))
        #Key is published to topic. Most vulnerable point of the whole system is this topic.
        client.publish("KEY1", key)
        print(key)
        break

    while keypress:
        time.sleep(0.3)
        keypress_1 = keyboard.is_pressed("e")
        if keypress_1: #Here we're concluding the user has held the button for more than a second.
            client.publish("DOORBELL1-PUB", f"{temp[2]} - {key}")
            print(f"{temp[2]} - {key}")
            os.system(f"python3 {os.getcwd()}/Publisher.py")
            exit()
        elif ~keypress_1: #Now, the button was pressed once and then let go.
            print("WAITING FOR NEW INPUT")
            time.sleep(0.5)
            keypress_2 = keyboard.is_pressed("e")
            if keypress_2: #Here we're concluding the user has held the button for more than a second.
                client.publish("DOORBELL1-PUB", f"{temp[3]} - {key}")
                print(f"{temp[3]} - {key}")
                os.system(f"python3 {os.getcwd()}/Publisher.py")
                exit()
            elif ~keypress_2: #Now, the button was pressed once and then let go.
                client.publish("DOORBELL1-PUB", f"{temp[1]} - {key}")
                print(f"{temp[1]} - {key}")
                os.system(f"python3 {os.getcwd()}/Publisher.py")
                exit()