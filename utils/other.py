import os

__SLEEP__ = 3

__LOGO__ = r"""
 _____
|__  /  Whatsapp Group Logo Creator
  / /   for RIS Kurunegala
 / /_   v1.0
/____|  Made by @hirusha-adi
"""

__CREDITS__ = r"""
Made by Hirusha Adikari
"""

__MAIN_MENU__ = r"""
    [1] Start Web Server
    [2] Resize Images 
"""

__ResizeMenu__ = r"""
    [1] .jpg
    [2] .jpeg
    [3] .png
"""

if os.name == "nt":
    CLEAR = "cls"
    PIP = "pip"
    PYTHON = "python"
    SLASH = "\\"
else:
    CLEAR = "clear"
    PIP = "pip3"
    PYTHON = "python3"
    SLASH = "/"
