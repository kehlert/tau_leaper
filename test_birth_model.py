import unittest
from birth_model import BirthModel


class TestBirthModel(unittest.TestCase):
    def testConstructor(self):
        BirthModel()

    def testGetInitialStateReturnsCopy(self):
        model = BirthModel()
        initialState = dict(model.getInitialState())
        state = model.getInitialState()
        state['X'] = 0
        self.assertDictEqual(initialState, model.getInitialState())
