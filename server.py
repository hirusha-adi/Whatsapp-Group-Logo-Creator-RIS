import os

from flask import Flask, render_template, request, send_file

from utils.support import (fixImageName, getImages, makeImg_Style1,
                           makeImg_Style2)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        allimages = getImages()
        return render_template("index.html", allimages=allimages)

    if request.method == 'POST':
        topname = request.form.get('topname')
        middlename = request.form.get('middlename')
        bottomname = request.form.get('bottomname')
        stylename = request.form.get('stylename')
        imagename2Edit = fixImageName(imageName=request.form.get('imagename'))
        bgImg = os.path.join(os.getcwd(), "images", imagename2Edit)
        if stylename == "1":
            makeImg_Style1(title=topname, middle=middlename,
                           bottom=bottomname, filename=bgImg, savename="result.jpg")
        elif stylename == "2":
            makeImg_Style2(title=topname, middle=middlename,
                           bottom=bottomname, filename=bgImg, savename="result.jpg")
        return send_file('result.jpg', attachment_filename=f"{topname}-{middlename}-{bottomname}.jpg")


@app.route("/api", methods=['GET'])
def api():
    topname = request.args.get('top', default=None)
    middlename = request.args.get('middle', default=None)
    bottomname = request.args.get('bottom', default=None)
    stylename = request.args.get('style', default=None)
    imagename2Edit = fixImageName(
        imageName=request.args.get('image', default=None))
    bgImg = os.path.join(os.getcwd(), "images", imagename2Edit)
    if stylename == "1":
        makeImg_Style1(title=topname, middle=middlename,
                       bottom=bottomname, filename=bgImg, savename="result.jpg")
    elif stylename == "2":
        makeImg_Style2(title=topname, middle=middlename,
                       bottom=bottomname, filename=bgImg, savename="result.jpg")
    return send_file('result.jpg', attachment_filename=f"{topname}-{middlename}-{bottomname}.jpg")


@ app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3334, debug=False)
