import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "hi"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=3334, debug=True)
