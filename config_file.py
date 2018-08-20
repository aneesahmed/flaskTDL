# Example configuration
#http://flask.pocoo.org/docs/1.0/config/
import os

ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default=False)
if ENVIRONMENT_DEBUG.lower() in ("f", "false"):
    ENVIRONMENT_DEBUG = False

DEBUG = ENVIRONMENT_DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
if not SECRET_KEY:
    raise ValueError("No secret key set for Flask application")