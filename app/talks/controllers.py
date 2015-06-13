from flask import Blueprint, render_template, abort, send_from_directory
import json, os
from .. import app

talks = Blueprint('talks', __name__, url_prefix='/talks')

FILE_NAME = 'talks.json'

@talks.route('/')
def list():
  talks = load_talks()
  print talks['data']
  return render_template('talks.html', talks=talks['data'])

@talks.route("/adi-award")
def award():
  return send_from_directory(app.config['BASE_DIR'], "app/static/adi-award.pdf")

@talks.route('/<name>')
def talk(name):
  file_path = app.config['TEMPLATES_DIR'] + '/talks/' + name + ".html"
  try:
    return open(file_path, "r").read()
  except:
    abort(404)

def load_talks():
  file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),FILE_NAME)
  with open(file_path) as talks_file:
    return json.load(talks_file)