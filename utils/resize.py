import os
import sys

from PIL import Image


def jpg(filename: str, savename: str = "resized.jpg", width: int = 1024, height: int = 1024):
    if not(filename.lower().endswith(".jpg")):
        filename += ".jpg"

    if not(savename.lower().endswith(".jpg")):
        savename += ".jpg"

    try:
        imgjpg = Image.open(filename)
    except FileNotFoundError:
        sys.exit("No file found in " + str(os.getcwd()))
    except Exception as e:
        sys.exit("Error: " + str(e))

    imgjpg_resized = imgjpg.resize((width, height))
    imgjpg_resized.save(savename)
