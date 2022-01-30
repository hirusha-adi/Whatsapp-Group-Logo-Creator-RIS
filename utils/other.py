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
         ____  _     _                _                           _ _ 
        / __ \| |__ (_)_ __ _   _ ___| |__   __ _        __ _  __| (_)
       / / _` | '_ \| | '__| | | / __| '_ \ / _` |_____ / _` |/ _` | |
      | | (_| | | | | | |  | |_| \__ \ | | | (_| |_____| (_| | (_| | |
       \ \__,_|_| |_|_|_|   \__,_|___/_| |_|\__,_|      \__,_|\__,_|_|
        \____/                                                        
                        Whatsapp Group Logo Creator
                          made for RIS Kurunegala
                     Made by github user @hirusha-adi
                                   v1.0

                                MIT License

            Copyright (c) 2022 ZeaCeR#5641 (Hirusha Adikari)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__MAIN_MENU__ = r"""
    [1] Start Web Server
    [2] Resize Images
    [3] Download Stuff
    [4] Credits
    [5] Exit
"""

__ResizeMenu__ = r"""
    [1] .jpg
    [2] .jpeg
    [3] .png
"""

__LoadStuffMenu__ = r"""
    [1] Download Fonts
    [2] Download Images
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
