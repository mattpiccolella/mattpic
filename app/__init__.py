from flask import Flask, render_template, send_from_directory
from flask.ext.assets import Environment, Bundle
import os, json

app = Flask(__name__)

app.config.from_object('config.app_config')

from projects.controllers import projects as projects_module
app.register_blueprint(projects_module)

from talks.controllers import talks as talks_module
app.register_blueprint(talks_module)

ABOUT_FILE_NAME = "static/about.json"

# Prepare our assets
assets = Environment(app)
assets.url = app.static_url_path

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/resume")
def resume():
  return send_from_directory(app.config['BASE_DIR'], "app/static/resume.pdf")

@app.route("/about")
def about():
  about = load_about()
  return render_template('about.html', about=about['data'])

def load_about():
  file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),ABOUT_FILE_NAME)
  with open(file_path) as about_file:
    return json.load(about_file)