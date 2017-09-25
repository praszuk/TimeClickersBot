from Coords import Coords
from GameWindow import get_relative_point

from datetime import datetime
import time

from GrabScreen import grab_screen
from pyautogui import click, typewrite, pixelMatchesColor


class Game:
    relative_point = ()

    def __init__(self, relative_point=get_relative_point()):
        self.time_warp_counter = 0
        Game.relative_point = relative_point

# -------------- Actions -------------- #

    def start_game(self):
        print('TimeClickersBot has been started.')
        self.last_buying_time = time.time()
        self.session_start_time = datetime.now()

        while True:
            if check_time_warp() and abilities_are_active() is False:
                self.timeWarp()

            if time.time() - self.last_buying_time > 5:
                self.last_buying_time = time.time()
                buying(False)
            else:
                time.sleep(1)

    def timeWarp(self):
        self.time_warp_counter += 1
        _current_time = datetime.now()
        # [0:19]/[0:7] skipping miliseconds after dot withdate/without
        print(str(_current_time)[0:19],
              ' > TimeWarping #', self.time_warp_counter,
              ' Took: ', str(_current_time-self.session_start_time)[0:7],
              sep='')
        _img = grab_screen_in_game(*Coords.WHOLE_WINDOW)
        _img.save('../screenshots/TimeWarp_' +
                  str(self.time_warp_counter) + '.png', 'PNG')
        click_in_game(*Coords.TIME_WARP_B)           # Time warp Button
        time.sleep(2)
        click_in_game(*Coords.CONFIRM_YES_B)         # Confim Time warp
        time.sleep(2)
        click_in_game(*Coords.START_NEW_TIMELINE_B)  # Skipping artefacts
        time.sleep(6)
        self.clean_start()                           # Start again

    def clean_start(self):
        self.session_start_time = datetime.now()
        # Buying abilities and pistol upgrades
        click_in_game(*Coords.PISTOL_B, clicks=13, interval=0.1)
        time.sleep(.5)
        click_in_game(*Coords.TIME_WARP_B, clicks=10, interval=0.1)
        # Activate all abilities:
        typewrite(('space', '7', '0'), interval=0.1)
        # Hire each team member
        buying(True)
        # Set Idle Mode to true
        typewrite(('Q', 'W', 'E'), interval=0.1)
        # To prevent auto fake time warping cause delay of changing graphic.
        time.sleep(2)


def buying(reverse=False):
    keys = ('G', 'F', 'D', 'S', 'A')
    # After clean start keys must be in normal order to unlock guns
    if reverse:
        keys = reversed(keys)
    click_in_game(*Coords.FOCUS)
    typewrite(keys, interval=0.1)

# -------------- Check status of buttons -------------- #


def abilities_are_active():
    # checking points to prevent fake ready caused by:
    # - crosshair
    # - mouse moved (notification)
    # - other random thing

    points = [(Coords.A1), (Coords.A2), (Coords.A5), (Coords.A6)]

    for point in points:
        if pixel_color_in_game(*point, (255, 123, 0), tolerance=50):
            return True
    return False


def check_time_warp():
    if pixel_color_in_game(*Coords.TIME_WARP_A, (41, 255, 1), tolerance=40):
        return True
    return False

# -------------- Support for relative coords -------------- #


def click_in_game(x, y, clicks=1, interval=0.0, button='left'):
    x += Game.relative_point[0]
    y += Game.relative_point[1]
    click(x, y, clicks=clicks, interval=interval)


def grab_screen_in_game(x1, y1, x2, y2):
    x1 += Game.relative_point[0]
    y1 += Game.relative_point[1]
    x2 += Game.relative_point[0]
    y2 += Game.relative_point[1]
    return grab_screen(x1, y1, x2, y2)


def pixel_color_in_game(x, y, expectedRGBColor, tolerance=0):
    x += Game.relative_point[0]
    y += Game.relative_point[1]
    return pixelMatchesColor(x, y, expectedRGBColor, tolerance=tolerance)
