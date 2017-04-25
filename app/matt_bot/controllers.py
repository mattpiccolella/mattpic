from flask import Blueprint, render_template
import json, os
from .. import app

mattbot = Blueprint('matt-bot', __name__, url_prefix='/matt-bot')

@mattbot.route('/privacy-policy')
def privacy_policy():
  return render_template('privacy.html')