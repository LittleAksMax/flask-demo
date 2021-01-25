
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<usrname>/") # can pass variables with {{ value }} in the html file and as parameter we can pass in the name of the parameter/value we have in the html and give it a value
def user(usrname):
    return render_template("user.html", username=usrname) # cann put python code in by doing this {% expression %} as long as you end if with the appropriate {% %} (i.e. for ends in endfor)

#@app.route("/admin")
#def admin():
#    return redirect(url_for("index")) # function name as string

if __name__ == "__main__":
    app.run(debug=True)
