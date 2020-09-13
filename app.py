import os

from flask import Flask, flash, redirect, render_template


# Configure application
app = Flask(__name__)


# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/volunteer-art")
def volunteer_art():
    return render_template("volunteer_art.html")

@app.route("/volunteer-music")
def volunteer_music():
    return render_template("volunteer_music.html")
