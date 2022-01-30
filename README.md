# Whatsapp Group Logo Creator

Create whatsapp group logos/images quickly and easily

# Usage

- `main.py` file is made for resizing images, downloading fonts + images to another directory if needed + for testing purposes

- `server.py` is if the file to start the web server

## `/`

Self Explanatory Web User Interface

## `/api`

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Parameter Name</th>
    <th class="tg-0lax">Value</th>
    <th class="tg-0lax">Example</th>
    <th class="tg-0lax">Possible Values</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">top</td>
    <td class="tg-0lax">Top Text of the Image</td>
    <td class="tg-0lax">?top=10E</td>
    <td class="tg-0lax">*</td>
  </tr>
  <tr>
    <td class="tg-0lax">middle</td>
    <td class="tg-0lax">Middle Text of the Image</td>
    <td class="tg-0lax">?middle=RIS</td>
    <td class="tg-0lax">*</td>
  </tr>
  <tr>
    <td class="tg-0lax">bottom</td>
    <td class="tg-0lax">Bottom Text of the Image</td>
    <td class="tg-0lax">?bottom=2022</td>
    <td class="tg-0lax">*</td>
  </tr>
  <tr>
    <td class="tg-0lax">style</td>
    <td class="tg-0lax">Font Style</td>
    <td class="tg-0lax">?style=2</td>
    <td class="tg-0lax">1, 2</td>
  </tr>
  <tr>
    <td class="tg-0lax">image</td>
    <td class="tg-0lax">Background Image</td>
    <td class="tg-0lax">?image=Blue</td>
    <td class="tg-0lax">Blue, BlueLight, GreenDark, GreenLight, Orange, Purple, PurpleDark, Red, RedCloth, RedWall</td>
  </tr>
</tbody>
</table>

Possible Values for `image` are the file names(without the extension) inside `./images` directory

### Sample Usage:

- `http://ris.hirusha.xyz` - is the URL

```
http://ris.hirusha.xyz/api?top=10E&middle=RIS&bottom=2022&style=2&image=Blue
```

# Installation

## Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syyuu --noconfirm
sudo pacman -S git python python-pip --noconfirm
cd ~
git clone https://github.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS.git
cd ./Whatsapp-Group-Logo-Creator-RIS
pip3 install -r requirements.txt
python3 server.py # to start the web server
# CTRL + Z
# bg
# disown -h
```

## Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
cd ~
git clone https://github.com/hirusha-adi/Whatsapp-Group-Logo-Creator-RIS.git
cd ./Whatsapp-Group-Logo-Creator-RIS
pip3 install -r requirements.txt
python3 server.py # to start the web server
# CTRL + Z
# bg
# disown -h
```

## Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![image1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from this Github Reposotory

![image2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

3. Extract the downloaded `.zip` file
4. open `cmd` in that folder
5. run `pip install -r requirements.txt`
6. run `python server.py` to start the web server

# Screenshots

- `/`

  ![ss1](https://cdn.discordapp.com/attachments/877796755234783273/937195025077510204/unknown.png)
  ![ss2](https://cdn.discordapp.com/attachments/877796755234783273/937195083030216764/unknown.png)

- `/api`
  ![ss3](https://cdn.discordapp.com/attachments/877796755234783273/937195257756545074/unknown.png)

- `CLI`
  ![ss4](https://cdn.discordapp.com/attachments/877796755234783273/937195352598118410/unknown.png)
