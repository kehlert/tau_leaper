import unittest
from tau_leaper import TauLeaper
from birth_model import BirthModel


class TestConstructor(unittest.TestCase):
    def testConstructor(self):
        stepSize = 0.1
        endTime = 1
        TauLeaper(BirthModel(), stepSize, endTime)

    def testRun(self):
        stepSize = 0.1
        endTime = 1
        model = BirthModel()
        myLeaper = TauLeaper(model, stepSize, endTime)
        results = myLeaper.run()
        self.assertGreater(results['X'], model.getInitialState()['X'])
