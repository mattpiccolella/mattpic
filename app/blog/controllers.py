from flask import Blueprint, Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from .. import app
import sys, os

blog = Blueprint('blog', __name__, url_prefix='/blog')
flatpages = FlatPages(app)


@blog.route("/")
def list():
  posts = [p for p in flatpages]
  posts.sort(key=lambda item:item['date'], reverse=False)
  return render_template('blog.html', posts=posts)

@blog.route('/<name>')
def post(name):
  post = flatpages.get_or_404(name)
  return render_template('blog_post.html', post=post)