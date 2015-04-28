from flask import Flask, render_template, send_from_directory
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

app.config.from_object('config.app_config')

from blog.controllers import blog as blog_module
app.register_blueprint(blog_module)

from frisk.controllers import frisk as frisk_module
app.register_blueprint(frisk_module)

# Prepare our assets
assets = Environment(app)
assets.url = app.static_url_path

# Compile SCSS to CSS
scss = Bundle('scss/main.scss', depends='scss/*/*.scss', filters='pyscss', output='css/main.css')
assets.register('scss_main', scss)

# Compile JavaScript to minified version.
js = Bundle('js/base.js', 'js/jquery.js', filters='jsmin', output='js/main.js')
assets.register('js_main', js)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/resume")
def resume():
  return send_from_directory(app.config['BASE_DIR'], "app/static/resume.pdf")