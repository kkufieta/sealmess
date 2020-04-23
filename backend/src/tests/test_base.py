import unittest
from flask_sqlalchemy import SQLAlchemy
from ..views import app
from ..database import setup_db
from .config import customer_header, provider_header, owner_header

class BaseTestCase(unittest.TestCase):
    """This class represents the sealmess test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        setup_db(app)

        '''
        User profiles and headers:
            - Customer
            - Provider
            - Owner
        '''
        self.customer_header = customer_header
        self.provider_header = provider_header
        self.owner_header = owner_header

        '''
        Data for testing the application
        '''

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
            'menu_item_ids': [1]
        }

        self.order_add_menu_items = {
            'menu_item_ids': [1, 1]
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

    def check_401_header_missing(self, res, data):
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'authorization_header_missing: Authorization header is expected')

    def check_403(self, res, data):
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'forbidden: Permission not found')

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
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()