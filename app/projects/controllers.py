from flask import Blueprint, render_template, abort, send_from_directory
import json, os
from .. import app

projects = Blueprint('projects', __name__, url_prefix='/projects')

FILE_NAME = 'projects.json'

@projects.route('/')
def list():
  projects = load_projects()
  print projects['data']
  return render_template('projects.html', projects=projects['data'])

@projects.route('/<name>')
def talk(name):
  # Map the name to the project and then present the data we need.
  return "Not yet implemented"

def load_projects():
  file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),FILE_NAME)
  with open(file_path) as projects_file:
    return json.load(projects_file)