#!/usr/bin/env python3
from Coords import Cord

from datetime import datetime
import time

from GrabScreen import grab_screen
import numpy
from PIL import ImageOps

from pyautogui import click, typewrite

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
    image = ImageOps.grayscale(grab_screen(*Cord.tw))
    a = numpy.array(image.getcolors())
    a = a.sum()
    if 30000 <= a <= 32500:     # Grayscale of button
        return True
    else:
        return False


def abilitiesAreActive():
    # checking 3 points to prevent fake ready caused by:
    # - crosshair
    # - mouse moved (notification)
    # - other random thing

    points = [(*Cord.ability1, Cord.ability1[0]+1, Cord.ability1[1]+1),
              (*Cord.ability2, Cord.ability2[0]+1, Cord.ability2[1]+1),
              (*Cord.ability6, Cord.ability6[0]+1, Cord.ability6[1]+1)]

    sumOfPixels = []
    for point in points:
        img = ImageOps.grayscale(grab_screen(*point))
        a = numpy.array(img.getcolors())
        sumOfPixels.append(a.sum())

    for val in sumOfPixels:
        if val > 170:
            return True
    return False


def buying(first):
    keys = ('G', 'F', 'D', 'S', 'A')
    # After clean start keys must be in normal order to unlock guns
    if first:
        keys = reversed(keys)
    click(*Cord.game)
    typewrite(keys, interval=0.1)


def timeWarp():
    global counter
    counter += 1
    current_time = datetime.now()
    # [0:19]/[0:7] skipping miliseconds after dot withdate/without
    print(str(current_time)[0:19], ' > TimeWarping #', counter,
          ' Took: ', str(current_time-session_start_time)[0:7], sep='')
    img = grab_screen(*Cord.base)
    img.save('../screenshots/TimeWarp_' + str(counter) + '.png', 'PNG')
    click(*Cord.tw1)      # Time warp Button
    time.sleep(2)
    click(*Cord.yes)      # Confiming Time warp action
    time.sleep(2)
    click(*Cord.start)    # Skipping artefacts
    time.sleep(6)
    cleanStart()            # Start again


def cleanStart():
    global session_start_time
    session_start_time = datetime.now()
    # Buying abilities and pistol upgrades
    click(*Cord.pistol, clicks=13, interval=0.1)
    time.sleep(.5)
    click(*Cord.ability, clicks=10, interval=0.1)
    # Activate all abilities:
    typewrite(('space', '7', '0'), interval=0.1)
    # Hire each team member
    buying(True)
    # Set Idle Mode to true
    typewrite(('Q', 'W', 'E'), interval=0.1)
    # To prevent auto fake time warping cause delay of changing graphic.
    time.sleep(2)


main()
