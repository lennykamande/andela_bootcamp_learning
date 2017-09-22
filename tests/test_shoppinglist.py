# test_shoppinglist.py
import unittest
import os
import json
from app import create_app, db

class shoppinglistTestcase(unittest.TestCase):
    """This class represents the bucketlist test case"""