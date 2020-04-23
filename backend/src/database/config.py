import os

# LOCAL_DATABASE_NAME is set by running setup.sh
#   For local development, it uses the database name: sealmess
#   For local testing, it uses the database name: sealmess_test
database_name = os.environ.get('LOCAL_DATABASE_NAME')

# Enable debug mode.
DEBUG = True

if not os.environ.get('DATABASE_URL'):
    print('Connected to the database named: ', database_name)
    SQLALCHEMY_DATABASE_URI = "postgres://{}/{}".format('localhost:5432', database_name)
else:
    print('Found Herokus postgres url')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False



