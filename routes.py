from flask import Flask
from app import app

<<<<<<< HEAD
@app.route("/")
def index():
    return 'Hello, world!'
=======
@app.route("/certification")
def certification():
    return 'This is your certification list!'

@app.route("/achievement")
def achievement():
    return 'This is your achievement list!'

@app.route("/profile")
def profile():
    return 'This is your profile page!'
>>>>>>> 80e7f486fa83905a390b35625d3b28ce1d389279
