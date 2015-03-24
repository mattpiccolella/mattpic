from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

app.config.from_object('config.app_config')

from blog.controllers import blog as blog_module
app.register_blueprint(blog_module)

# Prepare our assets
assets = Environment(app)
assets.url = app.static_url_path

# Compile SCSS to CSS
scss = Bundle('scss/main.scss', filters='pyscss', output='css/main.css')
assets.register('scss_main', scss)

# Compile JavaScript to minified version.
js = Bundle('js/base.js', filters='jsmin', output='js/main.js')
assets.register('js_main', js)

@app.route("/")
def home():
  return render_template("index.html")