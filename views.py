from flask import Blueprint, render_template

view = Blueprint("view", __name__)


@view.route("/")
def hello_world():
    return render_template("index.html")