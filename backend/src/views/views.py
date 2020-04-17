from flask_sqlalchemy import SQLAlchemy
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

setup_db(app)

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()

@app.route('/')
def home():
    return jsonify({
        'success': True
    })