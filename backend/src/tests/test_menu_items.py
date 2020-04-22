import unittest
import json
from .shared import BaseTestCase
from ..database import MenuItem

class MenuItemTestCase(BaseTestCase):
    '''
    Tests: MenuItem (RBAC Provider)
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
        provider_id = self.menu_item['provider_id']
        res = self.client().post('/providers/' + str(provider_id) + '/menu',
                                 headers=self.provider_header,
                                 json=self.menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['menu_item'])
        self.assertIsInstance(data['menu_item'], dict)

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/providers/' + str(provider_id) +
                                   '/menu/' + str(created_id),
                                   headers=self.provider_header)
        data = json.loads(res.data)

        menu_item = MenuItem.query.filter(MenuItem.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertIsNone(menu_item)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /providers/1/menu -- Add a new menu-item to DB 
    def test_200_create_menu_item(self):
        provider_id = self.menu_item['provider_id']
        res = self.client().post('/providers/' + str(provider_id) + '/menu',
                                 headers=self.provider_header,
                                 json=self.menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['menu_item'])
        self.assertIsInstance(data['menu_item'], dict)

    # GET /providers/1/menu -- Get the menu of a provider
    #   Open to public
    def test_200_get_menu(self):
        provider_id = 1
        res = self.client().get('/providers/' + str(provider_id) + '/menu')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['menu'])
        self.assertIsNotNone(data['provider_id'])
        self.assertIsInstance(data['menu'], list)
        self.assertEqual(data['provider_id'], provider_id)

    # GET /providers/1/menu/1 -- Get a menu item
    #   Open to public
    def test_200_get_menu_item(self):
        provider_id = 1
        menu_item_id = 1
        res = self.client().get('/providers/' + str(provider_id) + 
                                '/menu/' + str(menu_item_id))
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['menu_item'])
        self.assertIsNotNone(data['provider_id'])
        self.assertIsNotNone(data['menu_item_id'])
        self.assertEqual(data['provider_id'], provider_id)
        self.assertEqual(data['menu_item_id'], menu_item_id)
        self.assertIsInstance(data['menu_item'], dict)
        self.assertEqual(data['menu_item']['provider_id'], provider_id)

    # PATCH /providers/<int: provider_id>/menu/<int: menu_item_id> - Edit & update a menu-item
    def test_200_patch_menu_item(self):
        provider_id = 1
        menu_item_id = 1
        res = self.client().patch('/providers/' + str(provider_id) + 
                                  '/menu/' + str(menu_item_id),
                                  headers=self.provider_header,
                                  json=self.patch_menu_item)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['menu_item'])
        self.assertIsNotNone(data['menu_item_id'])
        self.assertIsInstance(data['menu_item'], dict)
        self.assertEqual(data['menu_item']['provider_id'], provider_id)
        for key in self.patch_menu_item:
            self.assertEqual(data['menu_item'][key], self.patch_menu_item[key])
    
    # TODO: -- invalid actions that should throw an error:
    # All of the above for anyone else except RBAC Customer
        # Test for: public, Provider, Owner

    # POST /providers/<int: provider_id>/menu/<int: menu_item_id>
    def test_405_create_menu_item_not_allowed(self):
        res = self.client().post('/providers/1/menu/1',
                                 headers=self.provider_header,
                                 json=self.menu_item)
        data = json.loads(res.data)

        self.check_405(res, data)

    # PATCH /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
    # DELETE /providers/<int: provider_id>/menu/<int: menu_item_id> for invalid id
    def test_404_menu_item_does_not_exist(self):
        # PATCH - menu_item id doesn't exist
        res = self.client().patch('/providers/1/menu/1000',
                                  headers=self.provider_header,
                                  json=self.patch_menu_item)
        data = json.loads(res.data)

        self.check_404(res, data)

        # PATCH - provider id doesn't exist
        res = self.client().patch('/providers/1000/menu/1',
                                  headers=self.provider_header,
                                  json=self.patch_menu_item)
        data = json.loads(res.data)

        self.check_404(res, data)

        # DELETE - menu_item id doesn't exist
        res = self.client().delete('/providers/1/menu/1000',
                                   headers=self.provider_header)
        data = json.loads(res.data)

        self.check_404(res, data)

        # DELETE - provider id doesn't exist
        res = self.client().delete('/providers/1000/menu/1',
                                   headers=self.provider_header)
        data = json.loads(res.data)

        self.check_404(res, data)

    # Test POST, GET, PATCH, DELETE when unauthorized
    def test_401_header_missing(self):
        # POST
        provider_id = self.menu_item['provider_id']
        res = self.client().post('/providers/' + str(provider_id) + '/menu',
                                 json=self.menu_item)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # DELETE
        res = self.client().delete('/providers/1/menu/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # PATCH
        res = self.client().patch('/providers/1/menu/1', 
                                  json=self.patch_menu_item)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

    # Test POST, GET, PATCH, DELETE when forbidden
    def test_403_forbidden(self):
        # POST
        provider_id = self.menu_item['provider_id']
        res = self.client().post('/providers/' + str(provider_id) + '/menu',
                                 headers=self.customer_header,
                                 json=self.menu_item)
        data = json.loads(res.data)
        self.check_403(res, data)

        provider_id = self.menu_item['provider_id']
        res = self.client().post('/providers/' + str(provider_id) + '/menu',
                                 headers=self.owner_header,
                                 json=self.menu_item)
        data = json.loads(res.data)
        self.check_403(res, data)

        # DELETE
        res = self.client().delete('/providers/1/menu/1',
                                   headers=self.customer_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().delete('/providers/1/menu/1',
                                   headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # PATCH
        res = self.client().patch('/providers/1/menu/1',
                                  headers=self.customer_header
                                  json=self.patch_menu_item)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().patch('/providers/1/menu/1',
                                  headers=self.owner_header
                                  json=self.patch_menu_item)
        data = json.loads(res.data)
        self.check_403(res, data)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()