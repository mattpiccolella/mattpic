# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.getcwd())

TEMPLATES_DIR = os.path.join(BASE_DIR, "app/templates")

FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'blog/content'
POST_DIR = 'posts'