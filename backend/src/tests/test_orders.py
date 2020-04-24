import unittest
import json
from .test_base import BaseTestCase
from ..database import Order


class OrderTestCase(BaseTestCase):
    '''
    Tests: Order (RBAC Customer)
        - POST /customers/<int: customer_id>/order
        - GET /customers/<int: customer_id>/order
        - GET /customers/<int: customer_id>/order/<int: order_id>
        - DELETE /customers/<int: customer_id>/order/<int: order_id>

        Invalid actions that should throw an error:
        - Invalid authentication & identification
            - Test all above with public, provider, owner
        - POST /customers/<int: customer_id>/order/<int: order_id>
        - DELETE /customers/<int: customer_id>/order/<int: order_id> for invalid id
    '''
    # POST /customers/<int: customer_id>/orders -- Add a new order to DB
    # DELETE /customers/<int: customer_id>/orders/<int: order_id> -- Delete an
    # order

    def test_200_create_and_delete_order(self):
        customer_id = self.order['customer_id']
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 headers=self.customer_header,
                                 json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['order'])

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/customers/' + str(customer_id) +
                                   '/orders/' + str(created_id),
                                   headers=self.customer_header)
        data = json.loads(res.data)

        order = Order.query.filter(Order.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertIsNone(order)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /customers/<int: customer_id>/orders -- Add a new order to DB
    def test_200_create_order(self):
        customer_id = self.order['customer_id']
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 headers=self.customer_header,
                                 json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['order'])

        # Add a second order to test database
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 headers=self.customer_header,
                                 json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['order'])

    # POST /orders/<int:order_id> -- Add a new order to DB
    def test_200_add_menu_items_to_order(self):
        order_id = 1
        res = self.client().post('/orders/' + str(order_id) + '/menu_items',
                                 headers=self.customer_header,
                                 json=self.order_add_menu_items)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['order_id'])
        self.assertIsNotNone(data['order'])

    # GET /customers/<int: customer_id>/orders -- Get all orders from a
    # customer
    def test_200_get_all_orders(self):
        res = self.client().get('/customers/1/orders',
                                headers=self.customer_header)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['customer_id'])
        self.assertIsNotNone(data['orders'])
        self.assertIsInstance(data['orders'], list)

    # GET /customers/<int: customer_id>/orders/<int: order_id> -- Get order
    # details
    def test_200_get_order(self):
        res = self.client().get('/customers/1/orders/1',
                                headers=self.customer_header)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['customer_id'])
        self.assertIsNotNone(data['order_id'])
        self.assertIsNotNone(data['order'])
        self.assertIsInstance(data['order'], dict)

    # POST /customers/<int: customer_id>/orders/<int: order_id>
    def test_405_create_order_not_allowed(self):
        res = self.client().post('/customers/1/orders/1',
                                 headers=self.customer_header,
                                 json=self.order)
        data = json.loads(res.data)

        self.check_405(res, data)

    # DELETE /customers/<int: customer_id>/orders/<int: order_id> for invalid
    # id
    def test_404_order_does_not_exist(self):
        # PATCH
        res = self.client().delete('/customers/1/orders/1000',
                                   headers=self.customer_header)
        data = json.loads(res.data)

        self.check_404(res, data)

        # DELETE
        res = self.client().delete('/customers/1000/orders/1',
                                   headers=self.customer_header)
        data = json.loads(res.data)

        self.check_404(res, data)

    def test_401_header_missing(self):
        # POST
        customer_id = self.order['customer_id']
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 json=self.order)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # DELETE
        res = self.client().delete('/customers/1/orders/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # POST - add menu items to order
        res = self.client().post('/orders/1/menu_items',
                                 json=self.order_add_menu_items)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # GET orders
        res = self.client().get('/customers/1/orders')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # GET order
        res = self.client().get('/customers/1/orders/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

    # Test POST, GET, PATCH, DELETE when forbidden
    def test_403_forbidden(self):
        # POST
        customer_id = self.order['customer_id']
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 headers=self.owner_header,
                                 json=self.order)
        data = json.loads(res.data)
        self.check_403(res, data)

        customer_id = self.order['customer_id']
        res = self.client().post('/customers/' + str(customer_id) + '/orders',
                                 headers=self.provider_header,
                                 json=self.order)
        data = json.loads(res.data)
        self.check_403(res, data)

        # DELETE
        res = self.client().delete('/customers/1/orders/1',
                                   headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().delete('/customers/1/orders/1',
                                   headers=self.provider_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # POST - add menu items to order
        res = self.client().post('/orders/1/menu_items',
                                 headers=self.owner_header,
                                 json=self.order_add_menu_items)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().post('/orders/1/menu_items',
                                 headers=self.provider_header,
                                 json=self.order_add_menu_items)
        data = json.loads(res.data)
        self.check_403(res, data)

        # GET orders
        res = self.client().get('/customers/1/orders',
                                headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().get('/customers/1/orders',
                                headers=self.provider_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # GET order
        res = self.client().get('/customers/1/orders/1',
                                headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().get('/customers/1/orders/1',
                                headers=self.provider_header)
        data = json.loads(res.data)
        self.check_403(res, data)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
