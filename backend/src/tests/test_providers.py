import unittest
import json
from .test_base import BaseTestCase
from ..database import Provider


class ProviderTestCase(BaseTestCase):
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
        res = self.client().post('/providers',
                                 headers=self.provider_header,
                                 json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['provider'])
        self.assertIsInstance(data['provider'], dict)

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/providers/' + str(created_id),
                                   headers=self.provider_header)
        data = json.loads(res.data)

        provider = Provider.query.filter(
            Provider.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertIsNone(provider)
        self.assertEqual(data['deleted_id'], created_id)

    # POST /provider -- Add a new provider to DB
    def test_200_create_provider(self):
        res = self.client().post('/providers',
                                 headers=self.provider_header,
                                 json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['provider'])
        self.assertIsInstance(data['provider'], dict)

        # Add a second provider to test database
        res = self.client().post('/providers',
                                 headers=self.provider_header,
                                 json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['provider'])
        self.assertIsInstance(data['provider'], dict)

    # GET /providers -- Get a list of all providers
    #   Open to public
    def test_200_get_all_providers(self):
        res = self.client().get('/providers')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['providers'])
        self.assertIsInstance(data['providers'], list)

    # GET /providers/<int: provider_id> -- Get provider details
    #   Open to public
    def test_200_get_provider(self):
        res = self.client().get('/providers/1')
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['provider'])
        self.assertIsInstance(data['provider'], dict)

    # PATCH /providers/<int: provider_id> -- Edit & update a provider
    def test_200_patch_provider(self):
        id = 1
        res = self.client().patch('/providers/' + str(id),
                                  headers=self.provider_header,
                                  json=self.patch_provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['provider'])
        self.assertEqual(data['updated_id'], id)
        self.assertIsInstance(data['provider'], dict)
        for key in self.patch_provider:
            self.assertEqual(data['provider'][key], self.patch_provider[key])

    # POST /providers/<int: provider_id>
    def test_405_create_provider_not_allowed(self):
        res = self.client().post('/providers/1',
                                 headers=self.provider_header,
                                 json=self.provider)
        data = json.loads(res.data)

        self.check_405(res, data)

    # PATCH /providers/<int: provider_id> for invalid id
    # DELETE /providers/<int: provider_id> for invalid id
    def test_404_provider_does_not_exist(self):
        # PATCH
        res = self.client().patch('/providers/1000',
                                  headers=self.provider_header,
                                  json=self.patch_provider)
        data = json.loads(res.data)

        self.check_404(res, data)

        # DELETE
        res = self.client().delete('/providers/1000',
                                   headers=self.provider_header)
        data = json.loads(res.data)

        self.check_404(res, data)

    '''
    Tests: RBAC Owner
        - DELETE /providers/<int: provider>
    '''
    # POST /providers -- Add a new provider to DB (provider RBAC)
    # DELETE /providers/<int: provider_id> -- Delete a provider (owner RBAC)

    def test_200_delete_provider_owner(self):
        # Create a question, test if it works properly
        res = self.client().post('/providers',
                                 headers=self.provider_header,
                                 json=self.provider)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['provider'])
        self.assertIsInstance(data['provider'], dict)

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/providers/' + str(created_id),
                                   headers=self.owner_header)
        data = json.loads(res.data)

        provider = Provider.query.filter(
            Provider.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertIsNone(provider)
        self.assertEqual(data['deleted_id'], created_id)

    # Test POST, GET, PATCH, DELETE when unauthorized
    def test_401_header_missing(self):
        # POST
        res = self.client().post('/providers',
                                 json=self.provider)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # DELETE
        res = self.client().delete('/providers/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # PATCH
        id = 1
        res = self.client().patch('/providers/1',
                                  json=self.patch_provider)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

    # Test POST, GET, PATCH, DELETE when forbidden
    def test_403_forbidden(self):
        # POST
        res = self.client().post('/providers',
                                 headers=self.owner_header,
                                 json=self.provider)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().post('/providers',
                                 headers=self.customer_header,
                                 json=self.provider)
        data = json.loads(res.data)
        self.check_403(res, data)

        # DELETE
        res = self.client().delete('/providers/1',
                                   headers=self.customer_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # PATCH
        res = self.client().patch('/providers/1',
                                  headers=self.owner_header,
                                  json=self.patch_provider)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().patch('/providers/1',
                                  headers=self.customer_header,
                                  json=self.patch_provider)
        data = json.loads(res.data)
        self.check_403(res, data)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
