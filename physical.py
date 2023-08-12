print("Sensors and Actuators")
import time
import serial.tools.list_ports


try:
    ser = serial.Serial(port="COM4", baudrate=9600)
    print("Connected")
except:
    print("Can not open the port")

relay0_ON = [0,6,0,0,0,255,200,91]
relay0_OFF = [0,6,0,0,0,0,136,27]

relay1_ON = [1,6,0,0,0,255,201,138]
relay1_OFF = [1,6,0,0,0,0,137,202]

relay2_ON = [2,6,0,0,0,255,201,185]
relay2_OFF = [2,6,0,0,0,0,137,249]

relay3_ON = [3,6,0,0,0,255,200,104]
relay3_OFF = [3,6,0,0,0,0,136,40]

relay4_ON = [4,6,0,0,0,255,201,223]
relay4_OFF = [4,6,0,0,0,0,137,159]

relay5_ON = [5,6,0,0,0,255,200,14]
relay5_OFF = [5,6,0,0,0,0,136,78]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)


relay22_ON = [15,6,0,0,0,255,200,164]
relay22_OFF = [15,6,0,0,0,0,136,228]

def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0
soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)


# while True:
#     print("TEST RELAY")
#     setDevice1(True)
#     time.sleep(2)
#     setDevice1(False)
#     time.sleep(2)
#     setDevice2(True)
#     time.sleep(2)
#     setDevice2(False)
#     time.sleep(2)
# while True:
#     print("TEST SENSOR")
#     print(readMoisture())
#     time.sleep(1)
#     print(readTemperature())
#     time.sleep(1)
ser.write(relay1_ON)
time.sleep(2)
ser.write(relay1_OFF)
time.sleep(2)