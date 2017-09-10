#!/usr/bin/env python3
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

settings in game:
- Simplified Notation (Default)
- Screen Shake OFF
- Custom Crosshair OFF
- Reduce Particles ON
- Post Screen Effects ON
- Night Mode OFF
- 30/60 Frame Per Seconds (Prefer 60)
"""
m = PyMouse()
k = PyKeyboard()

counter = 0
session_start_time = datetime.now()


def main():
    timer = time.time()
    while True:
        if checkTimeWarp() and abilitiesAreActive() is False:
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
    if 30000 <= a <= 32500:     # Grayscale of button
        return True
    else:
        return False


def abilitiesAreActive():
    # checking 3 points to prevent fake ready caused by crosshair
    arr = []
    image = ImageOps.grayscale(grab_screen(
        Cord.ability1[0], Cord.ability1[1],
        Cord.ability1[0]+1, Cord.ability1[1]+1))
    a = numpy.array(image.getcolors())
    arr.append(a.sum())
    image = ImageOps.grayscale(grab_screen(
        Cord.ability2[0], Cord.ability2[1],
        Cord.ability2[0]+1, Cord.ability2[1]+1))
    a = numpy.array(image.getcolors())
    arr.append(a.sum())
    image = ImageOps.grayscale(grab_screen(
        Cord.ability6[0], Cord.ability6[1],
        Cord.ability6[0]+1, Cord.ability6[1]+1))
    a = numpy.array(image.getcolors())
    arr.append(a.sum())
    for val in arr:
        if val > 170:
            return True
    return False


def buying(first):
    keys = ('G', 'F', 'D', 'S', 'A')
    # After clean start keys must be in normal order to unlock guns
    if first:
        keys = reversed(keys)
    m.click(Cord.game[0], Cord.game[1])
    for key in keys:
        k.tap_key(key)
        time.sleep(.1)


def timeWarp():
    global counter
    counter += 1
    current_time = datetime.now()
    # [0:19]/[0:7] skipping miliseconds after dot withdate/without
    print(str(current_time)[0:19], ' > TimeWarping #', counter,
          ' Took: ', str(current_time-session_start_time)[0:7], sep='')
    img = grab_screen(Cord.base[0], Cord.base[1], Cord.base[2], Cord.base[3])
    img.save('screenshots/TimeWarp_' + str(counter) + '.png', 'PNG')
    m.click(Cord.tw1[0], Cord.tw1[1])       # Time warp Button
    time.sleep(2)
    m.click(Cord.yes[0], Cord.yes[1])       # Confiming Time warp action
    time.sleep(2)
    m.click(Cord.start[0], Cord.start[1])   # Skipping artefacts
    time.sleep(6)
    cleanStart()


def cleanStart():
    global session_start_time
    session_start_time = datetime.now()
    # Buying abilities and pistol upgrades
    for i in range(13):
        m.click(Cord.pistol[0], Cord.pistol[1])
        time.sleep(.1)
    time.sleep(.5)
    for i in range(10):
        m.click(Cord.ability[0], Cord.ability[1])
        time.sleep(.1)
    # Activate all abilities:
    keys = (k.space, '7', '0')
    for key in keys:
        k.tap_key(key)
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
