import unittest
import json
from .shared import BaseTestCase
from ..database import Customer

class CustomerTestCase(BaseTestCase):
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
        res = self.client().post('/customers',
                                 headers=self.customer_header,
                                 json=self.customer)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['customer'])
        self.assertIsInstance(data['customer'], dict)

        # Save id of created question so we can delete it
        created_id = data['created_id']

        # Test if deleting a question works properly
        res = self.client().delete('/customers/' + str(created_id),
                                   headers=self.customer_header)
        data = json.loads(res.data)

        customer = Customer.query.filter(Customer.id == created_id).one_or_none()

        self.check_200(res, data)
        self.assertIsNone(customer)
        self.assertEqual(data['deleted_id'], created_id)
    
    
    # POST /customers -- Add a new customer to DB 
    def test_200_create_customer(self):
        # Create a question, test if it works properly
        res = self.client().post('/customers',
                                 headers=self.customer_header,
                                 json=self.customer)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['created_id'])
        self.assertIsNotNone(data['customer'])
        self.assertIsInstance(data['customer'], dict)

    # GET /customers/<int: customer_id> -- Get customer details
    def test_200_get_customer(self):
        res = self.client().get('/customers/1',
                                headers=self.customer_header)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['customer'])
        self.assertIsInstance(data['customer'], dict)

    # PATCH /customers/<int: customer_id> -- Edit & update a customer
    def test_200_patch_customer(self):
        id = 1
        res = self.client().patch('/customers/' + str(id),
                                  headers=self.customer_header,
                                  json=self.patch_customer)
        data = json.loads(res.data)

        self.check_200(res, data)
        self.assertIsNotNone(data['customer'])
        self.assertIsInstance(data['customer'], dict)
        self.assertEqual(data['updated_id'], id)
        for key in self.patch_customer:
            self.assertEqual(data['customer'][key], self.patch_customer[key])

    # TODO: -- invalid actions that should throw an error:
    # All of the above for anyone else except RBAC Customer
        # Test for: public, Provider, Owner

    # POST /customers/<int: customer_id>
    def test_405_create_customer_not_allowed(self):
        # Create a question, test if it works properly
        res = self.client().post('/customers/1',
                                 headers=self.customer_header,
                                 json=self.customer)
        data = json.loads(res.data)

        self.check_405(res, data)
        

    # PATCH /customers/<int: customer_id> with invalid id
    # DELETE /customers/<int: customer_id> with invalid id
    def test_404_customer_does_not_exist(self):
        # PATCH
        res = self.client().patch('/customers/1000',
                                  headers=self.customer_header,
                                  json=self.patch_customer)
        data = json.loads(res.data)

        self.check_404(res, data)

        # DELETE
        res = self.client().delete('/customers/1000',
                                   headers=self.customer_header)
        data = json.loads(res.data)

        self.check_404(res, data)

    # Test POST, GET, PATCH, DELETE when unauthorized
    def test_401_header_missing(self):
        # POST
        res = self.client().post('/customers',
                                 json=self.customer)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # DELETE
        res = self.client().delete('/customers/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # GET
        res = self.client().get('/customers/1')
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

        # PATCH
        id = 1
        res = self.client().patch('/customers/1',
                                  json=self.patch_customer)
        data = json.loads(res.data)
        self.check_401_header_missing(res, data)

    # Test POST, GET, PATCH, DELETE when forbidden
    def test_403_forbidden(self):
        # POST
        res = self.client().post('/customers',
                                 headers=self.owner_header,
                                 json=self.customer)
        data = json.loads(res.data)
        print(data)
        self.check_403(res, data)

        res = self.client().post('/customers',
                                 headers=self.provider_header,
                                 json=self.customer)
        data = json.loads(res.data)
        self.check_403(res, data)

        # DELETE
        res = self.client().delete('/customers/1',
                                   headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().delete('/customers/1',
                                   headers=self.provider_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # GET
        res = self.client().get('/customers/1',
                                headers=self.owner_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().get('/customers/1',
                                headers=self.provider_header)
        data = json.loads(res.data)
        self.check_403(res, data)

        # PATCH
        res = self.client().patch('/customers/1',
                                  headers=self.owner_header,
                                  json=self.patch_customer)
        data = json.loads(res.data)
        self.check_403(res, data)

        res = self.client().patch('/customers/1',
                                  headers=self.provider_header,
                                  json=self.patch_customer)
        data = json.loads(res.data)
        self.check_403(res, data)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()