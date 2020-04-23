import os
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(os.path.abspath(__file__))

# Enable debug mode.
DEBUG = True

if not os.environ.get('DATABASE_URL'):
    print('can not find Herokus postgres url')
    database_name = "sealmess"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)
    SQLALCHEMY_DATABASE_URI = database_path
else:
    print('Found Herokus postgres url')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False



