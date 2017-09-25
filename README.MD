# Python TimeClickersBot
TimeClickersBot can help you farm Time Cubes or Time Weapons.

### How it works?
It's buying *Team Members* and it's waiting until your bonus time will be ended and you will get some Time Cubes. Then it makes *Time Warp* and starting over again.

This program is for players, who have at least **Defender 10**  achievement unlocked. Of course it can be used without it, but it can not be efficient.

The main strategy is investing in skills: **Starting Gold** and **Abilities Duration**.
More in the [Features section](#features).

*Note: Currently only for Linux*

### Installation
1. Download the newest version from [here](https://github.com/praszuk/TimeClickersBot/archive/master.zip).
2. Extract files to a directory.
3. You need at least Python3.5 and Python package manager, i.e. [pip](https://pip.pypa.io/en/stable/quickstart/) (you should own it if you have installed python) to install required packages.
    - In console just go to project directory and type ```pip install -r requirements.txt```. You can also use [Virtualenv](https://virtualenv.pypa.io/en/stable/).
    - TimeClickersBot uses [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) module. To work properly, you need to install some packages, depending on your operating system. How to install [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html).
4. [Linux]:
    - Program uses _xwininfo_ shell tool to get the position of the window. You should have installed it by default. Check it in terminal ```xwininfo -help```. If you have not, install it or use special arguments to pass coordinates of the window (TODO).

### Setup
- App 1280x768 windowed mode.
- The Program should automatically detect upper-left corner. If not, check dependencies or pass additional arguments with the coordinates of the window (TODO - Currently edit Game.py/GameWindow.py file xD).

Settings in game:
- Simplified Notation (Default).
- Screen Shake OFF.
- Custom crosshair OFF.
- Reduce Particles ON.
- Post Screen Effects OFF - It looks ugly, but it is the most important setting.
- Night Mode OFF.
- 30/60 Frame Per Seconds.

If everything was set:
- Go to TimeClickersBot/src/ directory and launch *Main* (in console).

### Features
- Auto-buying.
- Auto-detection position of the window on launch application.
- Auto-Time-Warping (with buying pistol, abilities and team members).
- Checking if Time Warp is available (if some Time Cubes were gathered).
- Checking if abilities are active.
- Logging in console Time Warps with date and duration time of session.
- Saving screenshots to file of last level before Time Warped.
