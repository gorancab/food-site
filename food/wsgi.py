import logging
import sys

from food import flask_app

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/gcab_pythonanywhere_com')

application = flask_app