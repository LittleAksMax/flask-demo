from flask import Blueprint, render_template

# set up blueprint: name (should be same as file), second is the file itself (__name__), then the path to the template and static folders
second = Blueprint("second", __name__, static_folder="static", template_folder="templates") # can also set template and static folder with Flask()

@second.route("/home")
@second.route("/")
def index():
    return "<h1>Hello, admin!</h1>"