#!/usr/bin/python3
""" Amenity unittest """
import unittest
from models.amenity import Amenity
import pep8

class Amenity_testing(unittest.TestCase):
    """func that test BaseModel """

    def testpep8(self):
        """func that  test codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
