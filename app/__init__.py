from flask import Flask, render_template, send_from_directory
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

app.config.from_object('config.app_config')

from projects.controllers import projects as projects_module
app.register_blueprint(projects_module)

from talks.controllers import talks as talks_module
app.register_blueprint(talks_module)

# Prepare our assets
assets = Environment(app)
assets.url = app.static_url_path

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/resume")
def resume():
  return send_from_directory(app.config['BASE_DIR'], "app/static/resume.pdf")