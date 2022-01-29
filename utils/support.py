import os
import sys

from PIL import Image, ImageDraw, ImageFont
from .other import SLASH

_all_files = os.listdir(os.path.join(os.getcwd(), "images"))
_allimages = []
for image in _all_files:
    if image.lower().endswith(".jpg"):
        _allimages.append(image.split(".jpg")[0])
    elif image.lower().endswith(".jpeg"):
        _allimages.append(image.split(".jpeg")[0])
    elif image.lower().endswith(".png"):
        _allimages.append(image.split(".png")[0])


def getImages():
    if isinstance(_allimages, list):  # final check
        return _allimages


def fixImageName(imageName: str = None):
    if imageName is None:
        sys.exit("Error: 'imageName' argument not passed to 'fixImageName()'")

    if imageName + ".jpg" in _all_files:
        return imageName + ".jpg"

    elif imageName + ".jpeg" in _all_files:
        return imageName + ".jpeg"

    elif imageName + ".png" in _all_files:
        return imageName + ".png"


def makeImg_Style1(title: str = None,
                   middle: str = None,
                   bottom: str = None,
                   filename: str = None,
                   savename: str = None
                   ):

    if savename is not None:
        if not(savename.lower().endswith(".jpg")):
            savename += ".jpg"
    else:
        sys.exit(
            "Error: 'savename' arguemnt not passed when calling 'makeImg_Style1()'")

    if not(filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg") or filename.lower().endswith(".png")):
        filename = fixImageName(imageName=filename)

    img = Image.open(filename)

    drawimg = ImageDraw.Draw(img)
    mainFont = ImageFont.truetype("fonts" + SLASH + "trajan.ttf", 180)
    yearFont = ImageFont.truetype("fonts" + SLASH + "trajan.ttf", 90)

    # Title
    if len(title) <= 2:
        title_pos = 400, 300
    else:
        title_pos = 355, 300
    drawimg.text(title_pos, title, "white", font=mainFont)

    # Middle
    if len(middle) <= 3:
        middle_pos = 350, 480
    else:
        middle_pos = 200, 480
    drawimg.text(middle_pos, middle, "white", font=mainFont)

    # Bottom
    if len(bottom) <= 4:
        bottom_pos = 410, 670
    else:
        bottom_pos = 300, 670
    drawimg.text(bottom_pos, bottom, "white", font=yearFont)

    img.convert("RGB").save(savename, 'JPEG')


def makeImg_Style2(title: str = None,
                   middle: str = None,
                   bottom: str = None,
                   filename: str = None,
                   savename: str = None
                   ):

    if savename is not None:
        if not(savename.lower().endswith(".jpg")):
            savename += ".jpg"
    else:
        sys.exit(
            "Error: 'savename' arguemnt not passed when calling 'makeImg_Style1()'")

    if not(filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg") or filename.lower().endswith(".png")):
        filename = fixImageName(imageName=filename)

    img = Image.open(filename)

    drawimg = ImageDraw.Draw(img)
    mainFont = ImageFont.truetype("fonts" + SLASH + "futura.ttf", 180)
    yearFont = ImageFont.truetype("fonts" + SLASH + "futura.ttf", 90)

    # Title
    if len(title) <= 2:
        title_pos = 400, 300
    else:
        title_pos = 340, 300
    drawimg.text(title_pos, title, "white", font=mainFont)

    # Middle
    if len(middle) <= 3:
        middle_pos = 370, 480
    else:
        middle_pos = 200, 480
    drawimg.text(middle_pos, middle, "white", font=mainFont)

    # Bottom
    if len(bottom) <= 4:
        bottom_pos = 400, 670
    else:
        bottom_pos = 300, 670
    drawimg.text(bottom_pos, bottom, "white", font=yearFont)

    img.convert("RGB").save(savename, 'JPEG')
