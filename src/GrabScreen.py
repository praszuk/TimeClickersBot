import ctypes
import platform
from PIL import Image
from pyautogui import screenshot


path = 'C/prtscn.so'
grab = ctypes.CDLL(path)


def grab_screen(x1, y1, x2, y2):
    if platform.system() == 'Linux':
        return grab_screen_linux(x1, y1, x2, y2)
    else:
        return screenshot(region=(x1, y1, x2, y2))


"""
It's function only for linux
Compiled from C it has better performance than pyautogui.
- From doc. pyautogui has ~10FPS with 1920x1080
- From testing program in C has ~20 FPS with 1920x1080
"""


def grab_screen_linux(x1, y1, x2, y2):
    w, h = x2-x1, y2-y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte*objlength)()

    grab.getScreen(x1, y1, w, h, result)

    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)
