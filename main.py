__author__ = "hirusha-adi"
__version__ = "1.0"

import os
import sys
import time

from server import app
from utils.other import (__CREDITS__, __LOGO__, __MAIN_MENU__, __SLEEP__,
                         __ResizeMenu__)
from utils.resize import jpeg, jpg, png


def ENTIRE_PROGRAM():
    print(__LOGO__)
    print(__MAIN_MENU__)

    # main menu option
    mmo = input("[?] Select an option[1-2]: ")

    # Start Web Server
    if mmo == "1":
        app.run("0.0.0.0", port=3334, debug=False)

    # Resize Images
    elif mmo == "2":
        print(__ResizeMenu__)
        mm1 = input("[?] Select an option[1-3]: ")

        mm1_filename = input("[?] Enter file name: ")
        mm1_savename = input("[?] Enter output save name [resized.jpg]: ")
        mm1_width = input("[?] Enter width [1024]: ")
        mm1_height = input("[?] Enter height [1024]: ")

        # Resize .jpg
        if mm1 == "1":
            jpg(filename=mm1_filename, savename=mm1_savename,
                width=int(mm1_width), height=int(mm1_height))

        # Resize .jpeg
        elif mm1 == "2":
            jpeg(filename=mm1_filename, savename=mm1_savename,
                 width=int(mm1_width), height=int(mm1_height))

        # Resize .png
        elif mm1 == "3":
            png(filename=mm1_filename, savename=mm1_savename,
                width=int(mm1_width), height=int(mm1_height))

        print("[+] Resized " + mm1_filename +
              " to Width-" + mm1_width + ", Height-" + mm1_width +
              " and saved to " + mm1_savename)
        time.sleep(__SLEEP__)


if __name__ == "__main__":
    while True:
        try:
            ENTIRE_PROGRAM()
        except (KeyboardInterrupt, SystemExit):
            break
