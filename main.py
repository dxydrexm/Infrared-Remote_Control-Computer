import serial
import pyautogui as ag
import time

"""
TODO (in order):
Arduino:
-   make the x leds light up if the mouseUp of x button is pressed (same for y)
-   make the crystal lcd screen show the sensitivity (maybe other useful information too)
-   make buttons to control the sensitivity or even a potentiometer ?
-   make a sound with a buzzer certain led light up when there's an issue or the max sensitivity is reached ?
-   use fingerprint recognition to lock or unlock the functionality ?
Python:
-    make a scroll-click button if possible
-    manage to make the clicks not as quick as they are
-    make the sensitivity more convenient to use
-    make the movements of the mouse more pleasant
-    find purpose for the two last empty buttons

other:
-   find max en lowest sens possible
"""

# Don't forget to change the port to yours
arduinoData = serial.Serial("com6", 9600)
sensitivity = 10

while True:
    while arduinoData.in_waiting == 0:
        pass
    mousePos = ag.position()

    dataPacket = str(arduinoData.readline()).strip("b'")
    print(dataPacket)

    if "CH-" in dataPacket:
        ag.click(button="left")
        time.sleep(0.5)
        continue

    if "CH+" in dataPacket:
        ag.click(button="right")
        time.sleep(0.5)
        continue

    if "VOL-" in dataPacket:
        ag.moveTo(mousePos[0]-sensitivity, mousePos[1]-sensitivity)
        continue

    if "VOL+" in dataPacket:
        ag.moveTo(mousePos[0], mousePos[1]-sensitivity)
        continue

    if "PLA" in dataPacket:
        ag.moveTo(mousePos[0]+sensitivity, mousePos[1]-sensitivity)
        continue

    if "MI" in dataPacket:
        ag.moveTo(mousePos[0]-sensitivity, mousePos[1])
        continue

    if "PLU" in dataPacket:
        pass

    if "EQ" in dataPacket:
        ag.moveTo(mousePos[0]+sensitivity, mousePos[1])
        continue

    if "0" in dataPacket:
        ag.moveTo(mousePos[0]-sensitivity, mousePos[1]+sensitivity)
        continue

    if "HU" in dataPacket:
        ag.moveTo(mousePos[0], mousePos[1]+sensitivity)
        continue

    if "tH" in dataPacket:
        ag.moveTo(mousePos[0]+sensitivity, mousePos[1]+sensitivity)
        continue

    if "1" in dataPacket:
        ag.mouseDown(button="left")
        continue

    if "2" in dataPacket:
        ag.scroll(sensitivity)
        continue

    if "3" in dataPacket:
        ag.mouseDown(button="right")
        continue

    if "4" in dataPacket:
        ag.mouseUp(button="left")
        continue

    if "5" in dataPacket:
        pass

    if "6" in dataPacket:
        ag.mouseUp(button="right")
        continue

    if "7" in dataPacket:
        sensitivity = sensitivity - 5
        continue

    if "8" in dataPacket:
        ag.scroll(-sensitivity)
        continue

    if "9" in dataPacket:
        sensitivity = sensitivity + 5
        continue
