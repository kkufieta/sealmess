from .shared import db
import json
    
'''
Provider, extends the base SQLAlchemy Model
'''
class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
        
    def __init__(self, name, address, phone, description):
        self.name = name
        self.address = address
        self.phone = phone
        self.description = description

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            provider = Provider(name=name, address=address,
                                phone=phone, description=description)
            provider.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a new model in a database
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
        deletes a new model from a database
        the model must exist in the database
        EXAMPLE
            provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
            if provider:
                provider.delete()
    '''
    def delete(self):
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
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'phone': self.phone,
            'order': self.order.format()
        }

    def __repr__(self):
        return json.dumps(self.format())