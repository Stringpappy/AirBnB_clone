#!/usr/bin/python3
"""unittest for city """
import unittest
from models.city import City
import pep8

class City_testing(unittest.TestCase):
    """ Test BaseModel """

    def testpep8(self):
        """ unit test for codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
