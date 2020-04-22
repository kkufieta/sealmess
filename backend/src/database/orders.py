from .shared import db
import json

'''
Association table for Order, connecting orders and menu_items
'''
order_items = db.Table('order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('menu_item_id', db.Integer, db.ForeignKey('menu_items.id'), primary_key=True),
)
    
'''
Order, extends the base SQLAlchemy Model
'''
class Order(db.Model):
    __tablename__ = 'orders'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Foreign key
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'),
                            nullable=False)

    # Attributes
    status = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(),
                           nullable=False)

    menu_items = db.relationship('MenuItem', secondary=order_items,
                                 backref=db.backref('orders', lazy=True))
        
    def __init__(self, customer_id, status, menu_items=[]):
        self.customer_id = customer_id
        self.status = status
        self.menu_items = menu_items

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            # menu_item_x is a MenuItem object
            order = Order(customer_id=customer_id, status=status,
                          menu_items=[menu_item_1, menu_item_2, ...])
            order.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    add_menu_item()
        add a new menu_item
        EXAMPLE
            order = Order.query.filter(Order.id == order_id).one_or_none()
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            if order and menu_item:
                order.add_menu_item(menu_item)
                order.update()
    '''
    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    '''
    empty_order()
        delete all menu_items from order
        EXAMPLE
            order = Order.query.filter(Order.id == order_id).one_or_none()
            if order:
                order.empty_order()
                order.update()
    '''
    def empty_order(self):
        self.menu_items = []

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            order = Order.query.filter(Order.id == order_id).one_or_none()
            if order:
                order.status = 'ready'
                order.update()
    '''
    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            order = Order.query.filter(Order.id == order_id).one_or_none()
            if order:
                order.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    format()
        format & return a model from the database as a json
        the model must exist in the database
        EXAMPLE
            print(order.format())
    '''
    def format(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'status': self.status,
            'created_at': str(self.created_at),
            'menu_items': [menu_item.format() for menu_item in self.menu_items]
        }

    def __repr__(self):
        return json.dumps(self.format())
