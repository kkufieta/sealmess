import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from .shared import app
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .errors import *
from .views import *


class SealMessTestCase(unittest.TestCase):
    """This class represents the sealmess test case"""

    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "sealmess_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(app, self.database_path)
        db_drop_and_create_all()

        self.customer = {
            'first_name': 'kat',
            'last_name': 'kittykat',
            'address': 'private street in brooklyn',
            'phone': 'xxx-xxx-xxxx'
        }

        self.patch_customer = {
            'first_name': 'Kat',
            'phone': 'yyy-yyy-yyyy'
        }

        self.provider = {
            'name': 'pizza heat',
            'address': 'pizza town',
            'phone': 'ppp-ppp-pppp',
            'description': 'Cheesiest pizza in town'
        }

        self.patch_provider = {
            'name': 'Pizza Hut',
            'description': 'Best pizza in town'
        }

        self.menu_item = {
            'provider_id': 1,
            'name': 'margarita pizza',
            'description': 'delicious',
            'price': 10.10,
            'image_link': "https://media.giphy.com/media/4ayiIWaq2VULC/giphy.gif"
        }

        self.patch_menu_item = {
            'name': "Pepperoni pizza",
            'price': 12.00
        }

        self.order = {
            'customer_id': 1,
            'status': 'eaten',
            'menu_item': self.menu_item
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    HTTP Method checks
    """

    def check_200(self, res, data):
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def check_400(self, res, data):
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def check_404(self, res, data):
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def check_405(self, res, data):
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def check_422(self, res, data):
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    def check_500(self, res, data):
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'internal server error')

    def check_503(self, res, data):
        self.assertEqual(res.status_code, 503)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'service unavailable')

    def test_200_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.check_200(res, data)

    '''
    def test_create_new_actor_casting_assistant(self):
        res = self.client().post('/actors',
                                 headers={"Authorization": "Bearer {}".format(self.casting_assistant)},
                                 json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], {'code': 'unauthorized', 'description':'Permission not found.'})

    def test_create_new_movies_executive_producer(self):
        res = self.client().post('/movies',
                                 headers={"Authorization": "Bearer {}".format(self.executive_producer)},
                                 json=self.movies)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movies_casting_assistant(self):
        res = self.client().post('/movies',
                                 headers={"Authorization": "Bearer {}".format(self.casting_assistant)},
                                 json=self.movies)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], {'code': 'unauthorized', 'description':'Permission not found.'})
    '''

    '''
    Tests: Customer (RBAC Customer)
        - POST /customers
        - GET /customers/<int: customer_id>
        - PATCH /customers/<int: customer_id>
        - DELETE /customers/<int: customer_id>

        Invalid actions that should throw an error:
        - All of the above for anyone else except RBAC Customer
            - Test for: public, Provider, Owner
        - POST /customers/<int: customer_id>
        - PATCH /customers/<int: customer_id> with invalid id
        - DELETE /customers/<int: customer_id> with invalid id
    '''
    # POST /customers -- Add a new customer to DB 
    # DELETE /customers/<int: customer_id> -- Delete a customer
    def test_200_create_and_delete_customer(self):
        # Create a customer, test if it works properly
        res = self.client().post('/customers', json=self.customer)
        data = json.loads(res.data)
        print('this is the result & data: ', res, data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['customer'])

        # Save id of created question so we can delete it
        created_id = data['created_id']
        print(created_id)

        # Test if deleting a question works properly
        res = self.client().delete('/customers/' + str(created_id))
        data = json.loads(res.data)
        print('trying to delete customer: ', res, data)

        customer = Customer.query.filter(Customer.id == created_id).one_or_none()
        print('customer: ', customer)

        self.check_200(res, data)
        self.assertEqual(customer, None)
        self.assertEqual(data['deleted_id'], created_id)
    
    
    # POST /customers -- Add a new customer to DB 
    def test_0_200_create_customer(self):
        # Create a question, test if it works properly
        res = self.client().post('/customers', json=self.customer)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['customer'])

    # GET /customers/<int: customer_id> -- Get customer details
    def test_200_get_customer(self):
        res = self.client().get('/customers/1')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['customer'])
        self.assertisinstance(data['customer'], dict)
        # TODO: check that returned customer is correct!

    # PATCH /customers/<int: customer_id> -- Edit & update a customer
    def test_200_patch_customer(self):
        res = self.client().patch('/customers/1', json=self.patch_customer)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['customer'])
        self.assertisinstance(data['customer'], dict)
        # TODO: check that returned customer is patched correctly!

    # TODO: -- invalid actions that should throw an error:
    # All of the above for anyone else except RBAC Customer
        # Test for: public, Provider, Owner

    # POST /customers/<int: customer_id>
    def test_405_create_customer_not_allowed(self):
        # Create a question, test if it works properly
        res = self.client().post('/customers/1', json=self.customer)
        data = json.loads(res.data)

        self.check_405(res, data)
        

    # PATCH /customers/<int: customer_id> with invalid id
    # DELETE /customers/<int: customer_id> with invalid id
    def test_422_customer_does_not_exist(self):
        # PATCH
        res = self.client().patch('/customers/1000', json=self.patch_customer)
        data = json.loads(res.data)

        self.check_422(res, data)

        # DELETE
        res = self.client().delete('/customers/1000')
        data = json.loads(res.data)

        self.check_422(res, data)

    '''
    Tests: Provider (RBAC Provider)
        - POST /providers
        - PATCH /providers/<int: provider_id>

    RBAC Provider, Owner:
        - DELETE /providers/<int: provider_id>
        
    Public:
        - GET /providers
        - GET /providers/<int: provider_id>

        Invalid actions that should throw an error:
            - Invalid authentication & identification
            - POST /providers/<int: provider_id>
            - PATCH /providers/<int: provider_id> for invalid id
            - DELETE /providers/<int: provider_id> for invalid id
        
    '''

    # POST /providers -- Add a new provider to DB
    # DELETE /providers/<int: provider_id> -- Delete a provider
    def test_200_create_and_delete_provider(self):
        # Create a question, test if it works properly
        res = self.client().post('/providers', json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/providers/' + str(created_id))
        data = json.loads(res.data)

        provider = Provider.query.filter(Provider.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertEqual(provider, None)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /provider -- Add a new provider to DB 
    def test_0_200_create_provider(self):
        res = self.client().post('/providers', json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['provider'])
        self.assertisinstance(data['provider'], dict)
        # TODO: Check that provider is added correctly

        # Add a second provider to test database
        res = self.client().post('/providers', json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['provider'])
        self.assertisinstance(data['provider'], dict)

    # GET /providers -- Get a list of all providers
    def test_200_get_all_providers(self):
        res = self.client().get('/providers')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['providers'])
        self.assertEqual(len(data['providers']), 2)
        # TODO: check that the list of providers is correct

    # GET /providers/<int: provider_id> -- Get provider details
    def test_200_get_provider(self):
        res = self.client().get('/providers/1')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.asserttrue(data['provider'])
        self.assertisinstance(data['provider'], dict)
        # TODO: check that returned customer is correct!

    # PATCH /providers/<int: provider_id> -- Edit & update a provider
    def test_200_patch_provider(self):
        res = self.client().patch('/providers/1', json=self.patch_provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.asserttrue(data['provider'])
        self.assertisinstance(data['provider'], dict)
        # TODO: check that returned provider is patched correctly!

    # POST /providers/<int: provider_id>
    def test_405_create_provider_not_allowed(self):
        res = self.client().post('/providers/1', json=self.provider)
        data = json.loads(res.data)

        self.check_405(res, data)

    # PATCH /providers/<int: provider_id> for invalid id
    # DELETE /providers/<int: provider_id> for invalid id
    def test_422_provider_does_not_exist(self):
        # PATCH
        res = self.client().patch('/providers/1000', json=self.patch_provider)
        data = json.loads(res.data)

        self.check_422(res, data)

        # DELETE
        res = self.client().delete('/providers/1000')
        data = json.loads(res.data)

        self.check_422(res, data)


    '''
    Tests: Menu (RBAC Provider)
        - POST /providers/<int: provider_id>/menu
        - PATCH /providers/<int: provider_id>/menu/<int: menu_item_id>

    RBAC Provider, Customer, Owner:
        - DELETE /providers/<int: provider_id>/menu/<int: menu_item_id>
        
    Public:
        - GET /providers/<int: provider_id>/menu
        - GET /providers/<int: provider_id>/menu/<int: menu_item_id>

        Invalid actions that should throw an error:
            - Invalid authentication & identification
            - POST /providers/<int: provider_id>/menu/<int: menu_item_id>
            - PATCH /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
            - DELETE /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
        
    '''
    # POST /providers/<int: provider_id>/menu -- Add a new menu-item to DB
    # DELETE /providers/<int: provider_id>/menu/<int: menu_item_id> - Delete a menu-item
    def test_200_create_and_delete_menu_item(self):
        # Create a question, test if it works properly
        res = self.client().post('/providers/1/menu', json=self.menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/providers/1/menu/' + str(created_id))
        data = json.loads(res.data)

        menu_item = MenuItem.query.filter(MenuItem.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertEqual(menu_item, None)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /providers/1/menu -- Add a new menu-item to DB 
    def test_0_200_create_menu_item(self):
        # Create a question, test if it works properly
        res = self.client().post('/providers/1/menu/', json=self.menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        # TODO: Check that menu item is added correctly

    # PATCH /providers/<int: provider_id>/menu/<int: menu_item_id> - Edit & update a menu-item
    def test_200_patch_menu_item(self):
        res = self.client().patch('/providers/1/menu/1', json=self.patch_menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.asserttrue(data['menu'])
        # TODO: check that returned menu-item is patched correctly!
    
    # TODO: -- invalid actions that should throw an error:
    # All of the above for anyone else except RBAC Customer
        # Test for: public, Provider, Owner

    # POST /providers/<int: provider_id>/menu/<int: menu_item_id>
    def test_405_create_menu_item_not_allowed(self):
        res = self.client().post('/providers/1/menu/1', json=self.menu_item)
        data = json.loads(res.data)

        self.check_405(res, data)

    # PATCH /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
    # DELETE /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
    def test_422_menu_item_does_not_exist(self):
        # PATCH
        res = self.client().patch('/providers/1/menu/1000', json=self.patch_menu_item)
        data = json.loads(res.data)

        self.check_422(res, data)

        # DELETE
        res = self.client().delete('/providers/1/menu/1000')
        data = json.loads(res.data)

        self.check_422(res, data)

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
    # DELETE /customers/<int: customer_id>/orders/<int: order_id> -- Delete an order
    def test_200_create_and_delete_order(self):
        # Create a question, test if it works properly
        res = self.client().post('/customers/1/orders', json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/customers/1/orders/' + str(created_id))
        data = json.loads(res.data)

        order = Order.query.filter(Order.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertEqual(order, None)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /customers/<int: customer_id>/orders -- Add a new order to DB
    def test_0_200_create_order(self):
        res = self.client().post('/customers/1/orders', json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['orders'])
        # TODO: Check that order is added correctly

        # Add a second order to test database
        res = self.client().post('/customers/1/orders', json=self.order)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['orders'])

    # GET /customers/<int: customer_id>/orders -- Get all orders from a customer
    def test_200_get_all_orders(self):
        res = self.client().get('/customers/1/orders')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['providers'])
        self.assertEqual(len(data['providers']), 2)
        # TODO: check that the list of providers is correct

    # GET /customers/<int: customer_id>/orders/<int: order_id> -- Get order details
    def test_200_get_order_details(self):
        res = self.client().get('/customers/1/orders/1')
        data = json.loads(res.data)

        self.check_200(res, data)
        # TODO: check that returned order is correct!


    # POST /customers/<int: customer_id>/orders/<int: order_id>
    def test_405_create_order_not_allowed(self):
        res = self.client().post('/customers/1/orders/1', json=self.order)
        data = json.loads(res.data)

        self.check_405(res, data)

    # DELETE /customers/<int: customer_id>/orders/<int: order_id> for invalid id
    def test_422_order_does_not_exist(self):
        # PATCH
        res = self.client().delete('/customers/1/orders/1000')
        data = json.loads(res.data)

        self.check_422(res, data)

    '''
    Tests: RBAC Owner
        - GET /providers
        - GET /providers/<int: provider_id>
        - DELETE /providers/<int: provider>
        (TODO: GET /statistics ... out of scope)
    '''
    # GET /providers -- Get all providers
    # GET /providers/<int: provider_id> -- Get details about a provider
    # DELETE /providers/<int: provider> -- Delete a provider


    '''
    def test_200_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['categories'])
        self.assertIsInstance(data['categories'], dict)

    def test_200_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(data['categories'])
        self.assertIsInstance(data['categories'], dict)

    def test_404_get_questions_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.check_404(res, data)

    def test_200_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertEqual(data['current_category'], 1)

    def test_404_get_questions_invalid_category_id(self):
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.check_404(res, data)

        res = self.client().get('/categories/-1/questions')
        data = json.loads(res.data)

        self.check_404(res, data)

    def test_404_get_questions_based_on_category_beyond_valid_page(self):
        res = self.client().get('/categories/3/questions?page=1000')
        data = json.loads(res.data)

        self.check_404(res, data)

    def test_200_get_questions_by_category_with_request_parameter(self):
        res = self.client().get('/categories/2/questions?page=1')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertEqual(data['current_category'], 2)

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post('/questions/1', json=self.new_question)
        data = json.loads(res.data)

        self.check_405(res, data)

        res = self.client().post('/questions/1000', json=self.new_question)
        data = json.loads(res.data)

        self.check_405(res, data)


    def test_422_delete_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.check_422(res, data)

    def test_400_invalid_search_term(self):
        res = self.client().post('/questions/search',
                                 json=self.invalidSearchTerm)
        data = json.loads(res.data)

        self.check_400(res, data)

    def test_200_search_for_question(self):
        res = self.client().post('/questions/search',
                                 json=self.searchTerm)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
        self.assertEqual(int(data['current_category']), 0)
        self.assertEqual(len(data['questions']), 1)

    def test_200_play_quiz(self):
        # Test with all categories
        res = self.client().post('/quizzes',
                                 json=self.play_quiz_json_category_all)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['question'])

        # Test with category 1
        res = self.client().post('/quizzes',
                                 json=self.play_quiz_json_category_1)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['question'])
        self.assertEqual(
            data['question']['id'],
            self.play_quiz_question_id_category_1)

        # Test with category 2
        res = self.client().post('/quizzes',
                                 json=self.play_quiz_json_category_2)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertTrue(data['question'])
        self.assertTrue(data['question']['id'] in
                        self.play_quiz_question_possible_ids_category_2)

    '''

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()