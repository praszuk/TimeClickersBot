import ctypes
from PIL import Image

path = "C/prtscn.so"
grab = ctypes.CDLL(path)


def grab_screen(x1, y1, x2, y2):
    w, h = x2-x1, y2-y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte*objlength)()

    grab.getScreen(x1, y1, w, h, result)

    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)
