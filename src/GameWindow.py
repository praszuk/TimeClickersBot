import platform

window_name = '"Time Clickers"'

""" Returning tuple (x, y) coordinates, upper left corner of the game,
without window decorators.

Function detects OS and use tools depending on it:
- Linux: xwininfo
- Mac OSX: AppleScript
- Windows: py32win

If system is not listed above, python reads coordinates from user.
"""


def get_relative_point():
    system = platform.system()
    # if system == 'Windows':
    #     pass    # TODO
    # elif system == 'Darwin':  # Mac OSX
    #     pass    # TODO
    if system == 'Linux':
        return _get_relative_point_linux()
    else:
        raise RuntimeError(system + ' is not supported.'
                           + 'Please launch app with'
                           + ' param to set x, y position of the window.')


""" Using xwininfo - Linux shell's tool to get (by name) information,
 about window, x and y position and resolution (without window decorators). """


def _get_relative_point_linux():
    import re
    import subprocess
    output = subprocess.getstatusoutput('xwininfo -name ' + window_name)

    #  Output '0' mean: "everything is ok, the program is executed correctly"
    #  Other values are error exit code.
    if output[0] == 0:
        pattern = 'Absolute\s*upper-left\s*[XY]:\s*([0-9]+)'
        search_result = re.findall(pattern, output[1], flags=0)
        # 2 values x and y position
        if len(search_result) == 2:
            try:
                return (int(search_result[0]), int(search_result[1]))
            except:
                pass
        raise AttributeError('Cannot parse x and y from xwininfo output!\n'
                             + 'Check if your window is not below the screen.')

    elif output[0] == 127:  # xwininfo is not installed
        raise MissingDependencies('xwininfo (Linux package)')
    else:
        raise DependencyError('xwininfo error('
                              + str(output[0])
                              + '): ' + output[1])

# ---------- Exceptions ---------- #


class MissingDependencies(Exception):
    def __init__(self, dependency):
        self.dependency = dependency

    def __str_(self):
        return repr(self.dependency)


class DependencyError(Exception):
    def __init__(self, dependency):
        self.dependency = dependency

    def __str_(self):
        return repr(self.dependency)
