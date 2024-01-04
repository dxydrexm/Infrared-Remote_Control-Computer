import serial

arduinoData = serial.Serial("com6", 9600)
while True:
    while arduinoData.in_waiting == 0:
        pass
    dataPacket = arduinoData.readline()
    print(dataPacket)
