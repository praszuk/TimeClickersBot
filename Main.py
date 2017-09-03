import time
from GrabScreen import grab_screen
from Coords import Cord
import numpy
from PIL import ImageOps
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from datetime import datetime
"""
app 1280x768 windowed moved to blocking by side and upper panel
(start pos on ubuntu 16.04)
first pixel of game(65,52)
last pixel of game(1344,819)

"""
m = PyMouse()
k = PyKeyboard()

counter = 0


def main():
    timer = time.time()
    while True:
        if checkTimeWarp() and checkIfOrange() is False:
            timeWarp()
        else:  # Wait until time warp will be available
            if time.time() - timer > 5:
                timer = time.time()
                buying(False)
            else:
                time.sleep(1)


def checkTimeWarp():
    image = ImageOps.grayscale(grab_screen(
        Cord.tw[0], Cord.tw[1], Cord.tw[2], Cord.tw[3]))
    a = numpy.array(image.getcolors())
    a = a.sum()
    if 30000 <= a <= 32500:
        # print('Sum grayscale of Time Warp button: ', a)
        return True
    else:
        return False


def checkIfOrange():
    image = ImageOps.grayscale(grab_screen(
        Cord.abili1[0], Cord.abili1[1], Cord.abili1[0]+1, Cord.abili1[1]+1))
    a = numpy.array(image.getcolors())
    a = a.sum()
    if a < 170:
        return False
    else:
        return True


def buying(first):
    # print('Buying team members')
    m.click(Cord.game[0], Cord.game[1])
    keys = ('G', 'F', 'D', 'S', 'A')
    if first:
        # After clean start keys must be in normal order to unlock guns
        keys = reversed(keys)
    for key in keys:
        k.tap_key(key)
        time.sleep(.1)


def timeWarp():
    print(datetime.now(), '   > TimeWarping #', counter)
    global counter
    counter += 1
    m.click(Cord.tw1[0], Cord.tw1[1])  # Time warp Button
    time.sleep(1)
    # print('Confirming')
    m.click(Cord.yes[0], Cord.yes[1])  # Confiming Time warp action
    time.sleep(2)
    # print('Skipping artefacts')
    m.click(Cord.start[0], Cord.start[1])
    # print('CleanStart')
    time.sleep(6)
    cleanStart()


def cleanStart():
    # print('Buying abilities and pistol upgrades')
    for i in range(13):
        m.click(Cord.pistol[0], Cord.pistol[1])
        time.sleep(.1)
    time.sleep(.5)
    for i in range(10):
        m.click(Cord.abili[0], Cord.abili[1])
        time.sleep(.1)
    # Activate all abilities:
    k.tap_key(k.space)
    time.sleep(.1)
    k.tap_key('7')
    time.sleep(.1)
    k.tap_key('0')
    time.sleep(.1)
    # Hire each team member
    buying(True)
    # Set Idle Mode to true
    keys = ('Q', 'W', 'E')
    for key in keys:
        time.sleep(.1)
        k.tap_key(key)
    # To prevent auto fake time warping cause delay of changing graphic.
    time.sleep(2)


main()
