
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/<usr>/") # the / allows us to go to this with a slash after without crashing, just nice to have
def user(usr):
    return f"Hello, {usr}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user"), usr="Admin") # function name as string, name of param, as parameter

if __name__ == "__main__":
    app.run(debug=True)
