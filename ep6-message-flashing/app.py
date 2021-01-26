
from flask import Flask, redirect, url_for, render_template, request, session, flash # for flash messages
from datetime import timedelta # max time for session

app = Flask(__name__)
app.secret_key = "b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAMRPH2htqxNZTkLbRASwccAAAAEAAAAAEAAAIXAAAAB3NzaC1yc2EAAAADAQABAAACAQCsCYiU/3xB5iEyDHRplU7IRRowJD8Zo7K2mYOkPIg2flgc1pRZvGZlX+9nF0UJY8uXIUAsinXS6ya1sNSggXvqV/MdlTOMWQQnQT5yXSFu6aZr6ttWKcNzPDZUEm7X5zuS1uxHJcq0Tie4KPn3jS+SWF+aWeq5aQPeay2qz6Iw6twGGNzkkun+I0CvUbOvnWLs/OuRk3Jl2OWVpqVickMBOTcXsq6pdgEqe20mM9EkhFlX1QvUyetofNlkCZsbrOGVKpCDws0O/0z1Ctv5eRVJtuXVwz69FUHGWHE3TAURpRxaIvn74jgFVVegcWv+IN4WONZ+F0HZyyFzsD2xtYXIq44FQXdYMeLdLl5+SSyCChTvPXqEqlDlu+pT8jet2uuXiattdJKp7cP81J3NxOT1KnlJmGlskSQ9fwWeP36H5TcDWIRbsyqJqEA+f79Zcy48/4F7rVCfpsV+RGxjlNqf1uZEuZaLi774SnPRMPUQ9n1TI+oVX6BPgCtG9CrMUj/iaQVRfCl18bJW9zo20PmzriSW65UlzWh+ijjULBGHZ+XFIgfSdo7H3SW22nqqkZX1zVKr+97QezMyJ2rOr1FtS8U0fulmoC3/LcnwYuVT7xlUv4cgEUtJ+X6RX6D+HWj4Ih3n2O4fDgQQaE0HOJSoBseYwxvqCjFBuPcyGAEjQAAB2Dt6ErSnAAXKHrwc60VZ9pCIyRCjzDb6m1VXzOqF6jBlWZAO94JnmPkdDZH2gcBvabmeuDd6VJNfORGCWWWJVGb+02Gv4kSC/c58MzG8InSVJYbechPPHxoO1YHdWzSEFWh1qBnR8iu7lLKGxmn8pbHpxQraRu0dtOq8bh6IEvguxSKFQ56WV4be0dZycojZLxDDw9hHVmDtBPQAMXsZ7NYDn5AG70t1yD8SviQ/8wokcaJpS7crzdp4qm+Bs7W7gVDvQWSWin0i2nY8ivlV8mBNFEqUpNwYtqWlDqr2fScDYy/tKkJFrgBawxSPvi1PATfYpacHyQzf3dDoIHhS0XGEWYwR/G2n1/gjU/9uD/ueoBQnzpTfOGHW/3YtaI+HN4AR+348pmGGKgDdVU4NhYqL2r9Fme08WWJB5pgQjj9VlfbeH42j4R7olUruwAjc6ob3Y+SnLuOfZu5C4WZJr3VBxMnJ+mCU5BgyePI4BFfWupn7xUxyoIfM/qUnEGaUA3mv401FTUe4YbXqglrCNYEWg+/b+ui0A7NtDFDfx0rxmQSfsGP56NITjQwI239XFURm2jQxd/8kfvsTrfLvs8Nx8hOxly5nKimhI9xeWdigRYwtQHtl6iYsuEY+qzLpMV33ha+uSExcDUzJduL+FL4fUSdFRYizO2eZCbot/WOmIuyOb66Te3u5A5yBLbQkrxwTuwW91yNP6kM925uH3KLujm8v4PG/Uas8QfKzJNW158rz2+7iLhwHbTAm4JoGAmfCEKZhOqrdH2P6IMZYbyi8uheaPZUY+e/L03LHPGcVQV7JbKASWmw+lh/5zIeCthFqEXzCv1NSHtqFSLSf8nKVH1j7/ZtdSSdTK3ZLtYDKWkWzjefj2xJ5z5R76JaI/GUhu2y+gJb1R15462fszMNndroOtfsWf2eVqa+WvNibwmRXGyTaO//v7+q/SbOFE/n5uSOp9T4M26xi2fd7VQACm5xYqruH9ACTK8HutnrnslqKBov19wcVDMBwQOsuI5qT2PJyoE0EK8U0o/MuDp/kM7fMnUF+f5MKTNayofM6maNPYOWcMKJ2sehkoQvJWwqtIUZW2c0pE2tOepM37slSqj1E2syCPm51SMrFV/vWWrvX0GjPXVDEL7c3zFw+PHInMq154UvK3C/CMJs4WsdpVbTW9Kp3miynkBbG66FMlDqeHk4nusorB0/SlvK7OGcr46Agd28L9iKzWKt6YioJW6PYJbIzDvbV9sXtxX0zdauFFB1cBS1aaXsjS55l7xztVTt+IoUL69FR6bAdYjcRuhuIMQr50XU5wE99wDEknBS8KWOsErxloxdTvKCawqZIUE2ndxCaDIvbcY1KJmHgvTOXlucFZOJwy7GYce3O/Vho1Sy/IRsqCtMXbWAOyYvJRqDI5CtfmUBxxCjt8FTVanu+WTPktuWNKNZPCMqcdx1v+3e5QSpFq5tBUdMMjdyO9ibChdfMvQsSQtLgcXimAn63IbYscvYFqGjhjusILQtE53Oszvq7gZNYJ4m3bLBPgZzJZj8RfmCG+YpgrCejPMLB4bMb4xz/oeWycuDFwYO5OJfNQ2iPtcHARQY8Swpmt368On78lh6vgoP2HiwXdlsF9LYHZt2zEGYDJxjfMRKHZaaJ0zAE/CVazXp10L3NuTRgJvLBDdmcM3IpQzQ6xYWCx2CJIemHp1OiU6FajekCIiaN8S9daKyxmRK/Uy+F+cZ3+cKA3gT/lJf1cmKZolywvHZrDBfIRslrRaz02KkXWAbdyDL/D7M6WX+1fDGXr6A318sVZwTq+pfE1LSHLUOmn3h9z0ndZZpnSPqLP7TKKEl34NOHeWEA3yjyXlcDoGdIEzuU49541yNUPRujMv6gjqTrjXQTA/VsYtvNRUAA+NDhaJdUfZPcE/3dMAFCTEWeHEuVcFlqcWdA4tf27MKViqTJJIU6KLDGLMhcFgS6kXQUeZr0HV2WtWc34oEHTsGRmuTXdjFL7mJ4VHTGuGToUmBMQGM1cMc8BK0hMzuA6hSP9rpqSkxITHBn5GVTb/OOvT7BABhfLSM1JckV0zBTpFIn8tjGNRmBoFqNzgJaD75yZCeVdlOCwfovjIic5dcGGSW7bUyWO5gka/BsokFqnHUOwQX0tQBSnukSE+QPOba1i3clWKOZCqlPFBss3mB8Gfu+BotRFh+KewENcKqW/pVQPSfEGcvwNbDRZNpW++gyotvUr7j0JyzKtPobo5YlI8c9yT9b9YYBvZYn0CHO25OdfmeDBb1BE0Ucu9cbxscB12HolT+15JrfS+t+r8/r7HMBcB17Giy4Wk/l1j95U584wwE/m4ul6ANuK8HuhqM/la28qN3N2cdOrFcWvQb+pZRwOa1w9L/GsH6jgT9IOUKjUTZ7bzRD0hyP+xCjVtLkZUVkGX3S7Wvh0JfG41A7MnYdhVE3qCRvk1SPJuIxIp9ovAc+YriNHuEgEefvq3CGtVpUb/RjPX9RMjuJPT6nmRQEcO21nw7i/m4" # necessary step, used to encrypt and decrypt session info
app.permanent_session_lifetime = timedelta(days=1) # can also do minutes, hours, etc.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<usr>") 
def user(usr):
    if "user" not in session or session["user"] != usr: # check if this user is in the session
        return redirect(url_for("login")) # if user not in session they can go login page instead
    else:
        flash("You aren't logged in", "info")
        return render_template("user.html", usr=usr) 

@app.route("/login", methods=["GET", "POST"]) # methods we can use in the login page
def login():
    if request.method == "POST": # we got information and want to redirect to user
        # session.permanent = True # set permanent session, default by False
        user = request.form["username"] 
        session["user"] = user # a dictionary storing anything about the user
        flash("Logged in successfully", "info") # first param is the actual text displayed, second is type (info, error, warning)
        return redirect(url_for("user", usr=user))
    else: # we didn't click the submit button
        if "user" in session:
            flash("Logged in successfully", "info")
            return redirect(url_for("user", usr=session["user"])) # redirect to user page if in session
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        flash("{} has been logged out".format(session["user"]), "info")
    session.pop("user", None) # remove data
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
