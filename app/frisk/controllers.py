from flask import Blueprint, render_template

frisk = Blueprint('frisk', __name__, url_prefix='/stop-and-frisk')

@frisk.route("/")
def home():
  return render_template("frisk.html")

@frisk.route("/crimes")
def crimes():
  return render_template("crimes.html")

@frisk.route("/people")
def people():
  return render_template("people.html")

@frisk.route("/dates")
def dates():
  return render_template("dates.html")

@frisk.route("/precincts")
def precincts():
  return render_template("precincts.html")
