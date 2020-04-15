from flask_migrate import Migrate
from .shared import db
from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from .customers import Customer
from .providers import Provider

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    # Connect to the local Postgresql database
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
