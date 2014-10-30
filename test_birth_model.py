import unittest
from birth_model import BirthModel


class MyTestCase(unittest.TestCase):
    def testConstructor(self):
        a = BirthModel(5)
        self.assertEqual(5, a.doStuff())
