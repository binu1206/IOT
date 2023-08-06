import sys
from Adafruit_IO import MQTTClient
import time
# from uart import *
import random
from image_detect import *
from physical import *


AIO_FEED_ID = ["button1" ,"button2"]
AIO_USERNAME = "binu1206"
AIO_KEY = "aio_wcsG178tAV5Fim9gWXbepJl02xTZ"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed: "+ feed_id)
    if feed_id == "button1":
        if payload == "1":
            setDevice1(True)
        else:
            setDevice1(False)

    if feed_id == "button2":
        if payload == "1":
            setDevice2(True)
        else:
            setDevice2(False)




client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10 #state machine
counter_ai = 3
previous_ai = ""
ai_result = ""
counter_sensor1 = 5
counter_sensor2 = 5
counter_sensor3 = 5
counter_h = 5
counter_temp = 5
while True:
    print("Starting... counter",counter)
    counter = counter - 1
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 3
        previous_ai = ai_result
        ai_result = get_detection()
        if previous_ai != ai_result:
            client.publish("ai",ai_result)
    if counter <= 0:
        counter = 10
        print("Done")
    #     client.publish("sensor1", random.randint(10, 50))
    # if counter == 3 :
    #     client.publish("sensor2", random.randint(10, 100))
    # if counter == 5:
    #     client.publish("sensor3", random.randint(1000, 4000))
    time.sleep(1)
    counter_sensor1 -= 1
    if counter_sensor1 <= 0:
        counter_sensor1 = 10

    counter_sensor2 -= 1
    if counter_sensor2 <= 0:
        counter_sensor2 = 10
    counter_sensor3 -= 1
    if counter_sensor3 <= 0:
        counter_sensor3 = 10
    counter_h -= 1
    if counter_h <= 0:
        print(readMoisture())
        client.publish("sensor2",readMoisture())
    counter_temp -=1
    if counter_temp <= 0:
        print(readTemperature())
        Temp = readTemperature()/100
        client.publish("sensor1",Temp)
    # readSerial(client)
    time.sleep(1)

