from .shared import db
import json
    
'''
Menu-Item, extends the base SQLAlchemy Model
'''
class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Key
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'), nullable=False)
    
    # Attributes
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_link = db.Column(db.String(500))

    def __init__(self, provider_id, name, description, price, image_link):
        self.provider_id = provider_id
        self.name = name
        self.description = description
        self.price = price
        self.image_link = image_link

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            menu_item = MenuItem(provider_id=provider_id, name=name,
                                 description=description, price=price,
                                 image_link=image_link)
            menu_item.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            if menu_item:
                menu_item.price = 12.99
                menu_item.update()
    '''
    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            if menu_item:
                menu_item.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    format()
        format & return a model from the database as a json
        the model must exist in the database
        EXAMPLE
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            print(menu_item.format())
    '''
    def format(self):
        return {
            'id': self.id,
            'provider_id': self.provider_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_link': self.image_link
        }

    def __repr__(self):
        return json.dumps(self.format())