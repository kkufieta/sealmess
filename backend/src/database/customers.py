from .shared import db
import json

'''
Customer, extends the base SQLAlchemy Model
'''


class Customer(db.Model):
    __tablename__ = 'customers'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Attributes
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)

    # Child table: Orders
    orders = db.relationship('Order', backref='customers', lazy=True)

    def __init__(self, first_name, last_name, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            customer = Customer(first_name=first_name, last_name=last_name,
                                address=address, phone=phone)
            customer.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            if customer:
                customer.first_name = 'Kat'
                customer.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            if customer:
                customer.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    format()
        format & return a model from the database as a json
        the model must exist in the database
        EXAMPLE
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            print(customer.format())
    '''

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'phone': self.phone,
            'orders': [order.format() for order in self.orders]
        }

    def __repr__(self):
        return json.dumps(self.format())
