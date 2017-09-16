#!/usr/bin/env python3
from Coords import Cord

from datetime import datetime
import time

from GrabScreen import grab_screen
from pyautogui import click, typewrite, pixelMatchesColor

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
    if pixelMatchesColor(*Cord.TIME_WARP_A, (41, 255, 1), tolerance=40):
        return True
    else:
        return False


def abilitiesAreActive():
    # checking points to prevent fake ready caused by:
    # - crosshair
    # - mouse moved (notification)
    # - other random thing

    points = [(Cord.A1), (Cord.A2), (Cord.A5), (Cord.A6)]

    for point in points:
        if pixelMatchesColor(*point, (255, 123, 0), tolerance=50):
            return True
    return False


def buying(reverse=False):
    keys = ('G', 'F', 'D', 'S', 'A')
    # After clean start keys must be in normal order to unlock guns
    if reverse:
        keys = reversed(keys)
    click(*Cord.FOCUS)
    typewrite(keys, interval=0.1)


def timeWarp():
    global counter
    counter += 1
    current_time = datetime.now()
    # [0:19]/[0:7] skipping miliseconds after dot withdate/without
    print(str(current_time)[0:19], ' > TimeWarping #', counter,
          ' Took: ', str(current_time-session_start_time)[0:7], sep='')
    img = grab_screen(*Cord.WHOLE_WINDOW)
    img.save('../screenshots/TimeWarp_' + str(counter) + '.png', 'PNG')
    click(*Cord.TIME_WARP_B)             # Time warp Button
    time.sleep(2)
    click(*Cord.CONFIRM_YES_B)           # Confiming Time warp action
    time.sleep(2)
    click(*Cord.START_NEW_TIMELINE_B)    # Skipping artefacts
    time.sleep(6)
    cleanStart()                         # Start again


def cleanStart():
    global session_start_time
    session_start_time = datetime.now()
    # Buying abilities and pistol upgrades
    click(*Cord.PISTOL_B, clicks=13, interval=0.1)
    time.sleep(.5)
    click(*Cord.TIME_WARP_B, clicks=10, interval=0.1)
    # Activate all abilities:
    typewrite(('space', '7', '0'), interval=0.1)
    # Hire each team member
    buying(True)
    # Set Idle Mode to true
    typewrite(('Q', 'W', 'E'), interval=0.1)
    # To prevent auto fake time warping cause delay of changing graphic.
    time.sleep(2)


main()
