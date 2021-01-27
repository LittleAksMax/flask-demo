
from flask import Flask, redirect, url_for, render_template
from second import second as second # remind you of wsgi thing?

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin") # the prefix needs to come first, if present, the rest is sent to the blueprint

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)