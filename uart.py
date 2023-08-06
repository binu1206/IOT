print("Sensors and Actuators")

import time
import serial.tools.list_ports

try:
    ser = serial.Serial(port="COM3", baudrate=9600)
    print("Connected")
except:
    print("Can not open the port")
def sendCommand(cmd):
    ser.write(cmd.encode())

mess = ""

def processData(data, a, b):
    # print(data)
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        a["text"] = str(splitData[2])
    elif splitData[1] == "H":
        b.config(text=str(splitData[2]))
    #     client.publish("sensor1",splitData[2])
    # elif splitData[1] == "H":
    #     b["text"] = str(splitData[2])
    # #     client.publish("sensor2",splitData[2])
def readSerial(value1, value2):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")

        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(data=mess[start:end + 1], a=value1, b=value2)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end + 1:]

# while True:
#     readSerial()
#     time.sleep(1)