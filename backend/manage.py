from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.database import db
from src.views import app

def migrate(app, db):
    migrate = Migrate(app, db)

def get_manager(app, db):
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager

# How to use locally:
#   python3 manage.py db init --directory src/migrations/
#   python3 manage.py db migrate --directory src/migrations/
#   python3 manage.py db upgrade --directory src/migrations/
if __name__ == '__main__':
    migrate(app, db)
    manager = get_manager(app, db)
    manager.run()