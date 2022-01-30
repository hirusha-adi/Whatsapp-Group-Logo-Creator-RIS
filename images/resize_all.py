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


def jpeg(filename: str, savename: str = "resized.jpeg", width: int = 1024, height: int = 1024):
    if not(filename.lower().endswith(".jpeg")):
        filename += ".jpeg"

    if not(savename.lower().endswith(".jpeg")):
        savename += ".jpeg"

    try:
        imgjpeg = Image.open(filename)
    except FileNotFoundError:
        sys.exit("No file found in " + str(os.getcwd()))
    except Exception as e:
        sys.exit("Error: " + str(e))

    imgjpeg_resized = imgjpeg.resize((width, height))
    imgjpeg_resized.save(savename)


def png(filename: str, savename: str = "resized.png", width: int = 1024, height: int = 1024):
    if not(filename.lower().endswith(".png")):
        filename += ".png"

    if not(savename.lower().endswith(".png")):
        savename += ".png"

    try:
        imgpng = Image.open(filename)
    except FileNotFoundError:
        sys.exit("No file found in " + str(os.getcwd()))
    except Exception as e:
        sys.exit("Error: " + str(e))

    imgpng_resized = imgpng.resize((width, height))
    imgpng_resized.save(savename)


for filename in os.listdir(os.getcwd()):
    if filename.lower().endswith("jpg"):
        jpg(filename=filename, savename=filename, width=1024, height=1024)
    elif filename.lower().endswith("jpeg"):
        jpeg(filename=filename, savename=filename, width=1024, height=1024)
    elif filename.lower().endswith("png"):
        png(filename=filename, savename=filename, width=1024, height=1024)
