from .shared import db
import json

'''
Provider, extends the base SQLAlchemy Model
'''


class Provider(db.Model):
    __tablename__ = 'providers'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Attributes
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))

    # Child table: Menu items
    menu_items = db.relationship('MenuItem', backref='providers', lazy=True)

    def __init__(self, name, address, phone, description, image_link=''):
        self.name = name
        self.address = address
        self.phone = phone
        self.description = description
        self.image_link = image_link

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            provider = Provider(name=name, address=address,
                                phone=phone, description=description,
                                image_link=image_link)
            provider.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
            if provider:
                provider.name = 'Super Sushi'
                provider.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
            if provider:
                provider.delete()
    '''

    def delete(self):
        for menu_item in self.menu_items:
            menu_item.delete()
        db.session.delete(self)
        db.session.commit()

    '''
    format()
        format & return a model from the database as a json
        the model must exist in the database
        EXAMPLE
            provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
            print(provider.format())
    '''

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'description': self.description,
            'image_link': self.image_link
        }

    def __repr__(self):
        return json.dumps(self.format())
