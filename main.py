__author__ = "hirusha-adi"
__version__ = "1.0"

import os
import sys
import time

import requests

from server import app
from utils.other import (__CREDITS__, __LOGO__, __MAIN_MENU__, __SLEEP__,
                         __LoadStuffMenu__, __ResizeMenu__)
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
        mm1_savename = input("[?] Enter output save name [resized]: ")
        try:
            mm1_width = int(input("[?] Enter width [1024]: "))
        except ValueError:
            mm1_width = 1024
        try:
            mm1_height = int(input("[?] Enter height [1024]: "))
        except ValueError:
            mm1_height = 1024

        # Resize .jpg
        if mm1 == "1":
            jpg(filename=mm1_filename, savename=mm1_savename if str(mm1_savename).lower().strip() else "result.jpg",
                width=int(mm1_width), height=mm1_width)

        # Resize .jpeg
        elif mm1 == "2":
            jpeg(filename=mm1_filename, savename=mm1_savename if str(mm1_savename).lower().strip() else "result.jpeg",
                 width=int(mm1_width), height=int(mm1_height))

        # Resize .png
        elif mm1 == "3":
            png(filename=mm1_filename, savename=mm1_savename if str(mm1_savename).lower().strip() else "result.png",
                width=int(mm1_width), height=int(mm1_height))

        print("[+] Resized " + mm1_filename +
              " to Width-" + str(mm1_width) + ", Height-" + str(mm1_width) +
              " and saved to " + mm1_savename if str(mm1_savename).lower().strip() else "result")
        time.sleep(__SLEEP__)

    elif mmo == "3":
        print(__LoadStuffMenu__)
        mm3 = input("[?] Select an option[1-2]: ")
        if mm3 == "1":
            os.mkdir("fonts")
            os.chdir("fonts")
            futuraFont = requests.get(
                "https://github.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/raw/main/fonts/futura.ttf").content
            with open("futura.ttf", "wb") as futura:
                futura.write(futuraFont)

            trajanFont = requests.get(
                "https://github.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/raw/main/fonts/trajan.ttf").content
            with open("trajan.ttf", "wb") as trajan:
                trajan.write(trajanFont)

        if mm3 == "2":
            os.mkdir("images")
            os.chdir("images")

            imgData = (
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/Blue.jpg",
                 "Blue.jpg"),
                ("https://github.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/blob/main/images/BlueLight.jpg",
                 "BlueLight.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/GreenDark.jpg",
                 "GreenDark.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/GreenLight.jpeg",
                 "GreenLight.jpeg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/Orange.jpeg",
                 "Orange.jpeg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/Purple.jpg",
                 "Purple.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/PurpleDark.jpg",
                 "PurpleDark.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/Red.jpg",
                 "Red.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/RedCloth.jpg",
                 "RedCloth.jpg"),
                ("https://raw.githubusercontent.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS/main/images/RedWall.jpg",
                 "RedWall.jpg")
            )

            for imgLink, imgName in imgData:
                dataImg = requests.get(imgLink).content
                with open(f"{imgName}", "wb") as fileImg:
                    fileImg.write(dataImg)
                print("[+] Downloaded " + str(imgName) +
                      " and saved to ./images")


if __name__ == "__main__":
    while True:
        try:
            ENTIRE_PROGRAM()
        except (KeyboardInterrupt, SystemExit):
            break
