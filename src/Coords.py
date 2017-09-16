class Cord:
    # ------------------- General ------------------- #

    RESOLUTION = (1280, 768)        # Game resolution
    XY = (65, 52)  # TEMPORARY SET VALUE ON LINUX#Start point Left upper corner

    # ----------------- Area to get ----------------- #
    """ Whole game window i.e. to screenshot. """
    WHOLE_WINDOW = (XY[0], XY[1], XY[0]+RESOLUTION[0], XY[1]+RESOLUTION[1])

    """ Blue lines left/right to counting levels,
        Counter comapring screens,
        if at this coord lines are static blue,
        it means there is no animation of changing level.

        Two points with color: RGB(6, 102, 235) (tolerance 30)
        is enough, to know, if there are 2 static lines. """
    BLUE_LINE_L = (602+XY[0], 40+XY[1])  # , 602+XY[0], 75+XY[1])
    BLUE_LINE_R = (677+XY[0], 40+XY[1])  # , 677+XY[0], 75+XY[1])

    """ Time Warp button Area - to get color if is ready to time warp.
        Button has 2 states:
        - available  (light green): RGB(41, 255, 1) (tolerance 40)
        - unavailable (dark green): RGB(10, 64, 0)  (tolerance 40). """
    TIME_WARP_A = (1175+XY[0], 340+XY[1])

    """ All abilities 1-10. Diffrent coordinates to get color of point
    and check to get information about it status.

    Points below, should have this value:
    - activated (orange): RGB(255, 123, 0) (tolerance max 50)
    - available (blue):   RGB(0, 103, 255) (tolerance max 50)

    There is one more status "regeneration" RGB(0, 52, 128),
    but it's not needed. """

    A1 = (968+XY[0],  420+XY[1])  # , 968+XY[0],  421+XY[1])
    A2 = (1030+XY[0], 430+XY[1])  # , 1030+XY[0], 431+XY[1])
    A3 = (1091+XY[0], 430+XY[1])  # , 1091+XY[0], 431+XY[1])
    A4 = (1153+XY[0], 430+XY[1])  # , 1153+XY[0], 431+XY[1])
    A5 = (1214+XY[0], 430+XY[1])  # , 1214+XY[0], 431+XY[1])
    A6 = (968+XY[0],  484+XY[1])  # , 968+XY[0],  485+XY[1])
    A7 = (1030+XY[0], 484+XY[1])  # , 1030+XY[0], 485+XY[1])
    A8 = (1091+XY[0], 484+XY[1])  # , 1091+XY[0], 485+XY[1])
    A9 = (1153+XY[0], 484+XY[1])  # , 1153+XY[0], 485+XY[1])
    A0 = (1214+XY[0], 484+XY[1])  # , 1214+XY[0], 485+XY[1])

    # --------------- Area to click ----------------- #

    """ Buying pistol upgrade after reset. Just center of button. """
    PISTOL_B = (1215+XY[0], 245+XY[1])

    """ Time Warp/Unlock Abilities Button (center), to begin Time Warping. """
    TIME_WARP_B = (1215+XY[0], 345+XY[1])

    """ Start New Timeline (center), to start from beginning. """
    START_NEW_TIMELINE_B = (1130+XY[0], 360+XY[1])

    """ Confirming Time-Warping Button (center). """
    CONFIRM_YES_B = (530+XY[0], 550+XY[1])

    """ Void. It's only to get focus of game's window,
        without trigerring any unnecessary actions. """
    FOCUS = (960+XY[0], 320+XY[1])
