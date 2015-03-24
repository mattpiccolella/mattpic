from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route("/")
def hello():
  return "This is my first blog!"