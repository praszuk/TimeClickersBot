class Coords:

    # ------------------- General ------------------- #

    RESOLUTION = (1280, 768)

    # ----------------- Area to get ----------------- #

    """ Whole game window i.e. to screenshot. """
    WHOLE_WINDOW = (0, 0, RESOLUTION[0], RESOLUTION[1])

    """ Blue lines left/right to counting levels,
        Counter comparing screens,
        if at this coord lines are static blue,
        it means, there is no animation of changing level.

        Two points with color: RGB(6, 102, 235) (tolerance 30)
        is enough, to know, if there are 2 static lines. """
    BLUE_LINE_L = (602, 40)
    BLUE_LINE_R = (677, 40)

    """ Time Warp button Area - to get color if is ready to time warp.
        Button has 2 states:
        - available  (light green): RGB(41, 255, 1) (tolerance 40)
        - unavailable (dark green): RGB(10, 64, 0)  (tolerance 40). """
    TIME_WARP_A = (1175, 340)

    """ All abilities 1-10. Different coordinates to get color of point
    and check to get information about it status.

    Points below, should have this value:
    - activated (orange): RGB(255, 123, 0) (tolerance max 50)
    - available (blue):   RGB(0, 103, 255) (tolerance max 50)

    There is one more status "regeneration" RGB(0, 52, 128),
    but it's not needed. """

    A1 = (968,  420)
    A2 = (1030, 430)
    A3 = (1091, 430)
    A4 = (1153, 430)
    A5 = (1214, 430)
    A6 = (968,  484)
    A7 = (1030, 484)
    A8 = (1091, 484)
    A9 = (1153, 484)
    A0 = (1214, 484)

    # --------------- Area to click ----------------- #

    """ Buying pistol upgrade after reset. Just center of button. """
    PISTOL_B = (1215, 245)

    """ Time Warp/Unlock Abilities Button (center), to begin Time Warping. """
    TIME_WARP_B = (1215, 345)

    """ Start New Timeline (center), to start from beginning. """
    START_NEW_TIMELINE_B = (1130, 360)

    """ Confirming Time-Warping Button (center). """
    CONFIRM_YES_B = (530, 550)

    """ Void. It's only to get focus of game's window,
        without trigerring any unnecessary actions. """
    FOCUS = (960, 320)
