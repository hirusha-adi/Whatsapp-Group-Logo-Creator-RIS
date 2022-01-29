import os
import sys
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
