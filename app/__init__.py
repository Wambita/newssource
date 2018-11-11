from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
  """
    Function that initializes the flask application
  """
  # Initializing application
  app = Flask(__name__)

  # Creating app configs
  app.config.from_object(config_options[config_name])

  # Initializing flask extensions
  bootstrap.init_app(app)

  return app