
from flask import Flask, redirect, url_for, render_template, request, session # for sessions
from datetime import timedelta # max time for session

app = Flask(__name__)
app.secret_key = "AAAAAAAAAbq" # necessary step, used to encrypt and decrypt session info
app.permanent_session_lifetime = timedelta(days=1) # can also do minutes, hours, etc.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<usr>") 
def user(usr):
    if "user" not in session or session["user"] != usr: # check if this user is in the session 
        return redirect(url_for("login")) # if user not in session they can go login page instead
    else:
        return render_template("user.html", usr=usr) 

@app.route("/login", methods=["GET", "POST"]) # methods we can use in the login page
def login():
    if request.method == "POST": # we got information and want to redirect to user
        # session.permanent = True # set permanent session, default by False
        user = request.form["username"] 
        session["user"] = user # a dictionary storing anything about the user
        return redirect(url_for("user", usr=user))
    else: # we didn't click the submit button
        if "user" in session:
            return redirect(url_for("user", usr=session["user"])) # redirect to user page if in session
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None) # remove data
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
