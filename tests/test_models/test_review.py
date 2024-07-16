#!/usr/bin/python3
""" unittest fr  Review """
import unittest
from models.review import Review
import pep8

class Review_testing(unittest.TestCase):
    """ unitest for  BaseModel """

    def testpep8(self):
        """ test dor codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")i
