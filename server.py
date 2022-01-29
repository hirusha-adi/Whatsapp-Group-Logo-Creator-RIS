import os
import sys

from flask import Flask, render_template, request

from utils.support import fixImageName, getImages

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        allimages = getImages()

        return render_template("index.html", allimages=allimages)

    if request.method == 'POST':
        topname = request.form.get('topname')
        yearname = request.form.get('yearname')
        bottomname = request.form.get('bottomname')
        imagename = fixImageName(imageName=request.form.get('imagename'))

        return f"{topname}, {yearname}, {bottomname}, {imagename}"


@ app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3334, debug=True)
