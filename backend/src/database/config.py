import os
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(os.path.abspath(__file__))

database_name = "sealmess"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

# Enable debug mode.
DEBUG = True

SQLALCHEMY_DATABASE_URI = database_path
SQLALCHEMY_TRACK_MODIFICATIONS = False



