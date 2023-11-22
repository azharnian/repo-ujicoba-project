from flask import Flask
from app import app

@app.route("/certification")
def certification():
    return 'This is your certification list!'

@app.route("/achievement")
def achievement():
    return 'This is your achievement list!'

@app.route("/profile")
def profile():
    return 'This is your profile page!'