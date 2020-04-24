import unittest
import json
from .test_base import BaseTestCase


class HomeTestCase(BaseTestCase):
    '''
    Test: Home
        - This is mostly just a sanity check.
    '''

    def test_200_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.check_200(res, data)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
