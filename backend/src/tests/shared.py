import unittest
from flask_sqlalchemy import SQLAlchemy
from ..views import app
from ..database import setup_db

class BaseTestCase(unittest.TestCase):
    """This class represents the sealmess test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "sealmess_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(app, self.database_path)

        '''
        User profiles and headers:
            - Customer
            - Provider
            - Owner
        '''
        self.customer_access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoiT3daajVZUXFFN2tSUmhJNmY2S3RqbVdpMGdrMURwVGxAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NTkwNjg1LCJleHAiOjE1ODc2NzcwODUsImF6cCI6Ik93Wmo1WVFxRTdrUlJoSTZmNkt0am1XaTBnazFEcFRsIiwic2NvcGUiOiJwb3N0OmN1c3RvbWVyIGdldDpjdXN0b21lciBwYXRjaDpjdXN0b21lciBkZWxldGU6Y3VzdG9tZXIgcG9zdDpvcmRlciBnZXQ6b3JkZXIgZGVsZXRlOm9yZGVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicG9zdDpjdXN0b21lciIsImdldDpjdXN0b21lciIsInBhdGNoOmN1c3RvbWVyIiwiZGVsZXRlOmN1c3RvbWVyIiwicG9zdDpvcmRlciIsImdldDpvcmRlciIsImRlbGV0ZTpvcmRlciJdfQ.mDR2AuIQriP_Gw6RpvJML9f1zq_Y0htIIAxsYjL-KqaN2DH3xu5NIb6KtHjZKqGV6u28eWXWtZrk-uc8a14yfaRa-NH0EJUuL3oMbGa2EdvEAq16RQQqq65aMjbOtbCT1hN53EhDDobCq3HuI0NLBCzRvNpz46XJ5XiAlkhWE4xW-PQH75Al1RkW1RwXVXUS13hGGhx5e_IaHskY4i3ybC4pYW8-lXTB3TT8DCIJpHYvoJ8xocn_rVs7Tj66CChr5y30_N67RG6YdIvBWBj1lbd06CGEWJVyuXmraPa2xXVKQzF1ZaD6exHDkevBAFmGn6pOuwoNfEaDuEXUXc0dtA"
        self.provider_access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoiWVlRbUtaU0Q3MDVjbGJSQjdUekhYeEdtT0hpUkZHR2FAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NTkwNjY0LCJleHAiOjE1ODc2NzcwNjQsImF6cCI6IllZUW1LWlNENzA1Y2xiUkI3VHpIWHhHbU9IaVJGR0dhIiwic2NvcGUiOiJwb3N0OnByb3ZpZGVyIHBhdGNoOnByb3ZpZGVyIGRlbGV0ZTpwcm92aWRlciBwb3N0Om1lbnUgcGF0Y2g6bWVudSBkZWxldGU6bWVudSIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbInBvc3Q6cHJvdmlkZXIiLCJwYXRjaDpwcm92aWRlciIsImRlbGV0ZTpwcm92aWRlciIsInBvc3Q6bWVudSIsInBhdGNoOm1lbnUiLCJkZWxldGU6bWVudSJdfQ.JgtikU-TDT6wnVJjQNMXhT-51hAVxswWvtsL3cFPd7eTcnPN-DrS8TEXqul_fwuuSKsrvkApKJQ28MyUHr_Y5sBjEY_UDKQhEzA3A5G6ASYDtRiNS4fqvQTMVTH2lJxzshPTvUWhtKF75XRJnH7CHYhsQJSHfVL3HqhNbIusPwF8b8iCS-9AND-v3qN4AYE592k7wwQJZ1mIiXusvKt4i3-zNlE4miG8OF9kAe1vUL2_T01LAWpVFWSxI2IkjWEqtfJUBipb-F-kAnVJ2yBdYs53pZJ8C0OyQhWgQUVsTBAm8_1y1GlaVuCPQHYROU3RVLS_iV9p1TjiSptn1OMVtg"
        self.owner_access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoidXd6MHhVbWU0eXVaMHEyRmM5bW5FQkFoTkY1bjNIRHVAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NTkwNTA2LCJleHAiOjE1ODc2NzY5MDYsImF6cCI6InV3ejB4VW1lNHl1WjBxMkZjOW1uRUJBaE5GNW4zSER1Iiwic2NvcGUiOiJkZWxldGU6cHJvdmlkZXIiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvdmlkZXIiXX0.hgOI99nUqhpQN-Q4dhgBoZUHfNWu50hjti_AjLnLJHvJ7dpm2n44eQcrFJxN-PoqH9bvxYkjIfKBLtwmzSf5B5UVVNsqbvkZ8BmdUE-AwSCSSPdRzRfFhDdRkbpClNK1LVzDk_XEuOr6rMW0d4jnHkB0tdSvrVKWP1wvsRNzjenxUmUH1mbZUuwbPCzFbCgX520wqfYeq_QThpXIoY7BXC2ADw8brozDC8tcsZ26fqhcx1-IwSv-wggtILIkbwCYCOyroZuQyaRXfFnpiedzOC-3V1bfapeSs5euoGncQtVZC6ZjaDNu-GVkHz1XFXIaIbZ9ajXLYa86DF8wMpTyAw"

        self.customer_header = {"Authorization": "Bearer {}".format(self.customer_access_token)}
        self.provider_header = {"Authorization": "Bearer {}".format(self.provider_access_token)}
        self.owner_header = {"Authorization": "Bearer {}".format(self.owner_access_token)}

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