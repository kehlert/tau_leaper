import unittest
import numpy
from tau_leaper import TauLeaper
from birth_model import BirthModel
from dimer_model import DimerModel
from mean_accumulator import MeanAccumulator


class TestConstructor(unittest.TestCase):
    def testConstructor(self):
        stepSize = 0.1
        endTime = 1
        TauLeaper(BirthModel(), stepSize, endTime)

    def testSingleRun(self):
        stepSize = 0.001
        endTime = 5
        model = BirthModel()
        myLeaper = TauLeaper(model, stepSize, endTime)
        results = myLeaper.run()
        self.assertGreater(results['X'], model.getInitialState()['X'])

    def testMean(self):
        stepSize = 0.001
        endTime = 5
        model = BirthModel()
        myLeaper = TauLeaper(model, stepSize, endTime)

        accum = MeanAccumulator()
        nRuns = 10
        numpy.random.seed(0)
        for i in range(0, nRuns):
            accum.add(myLeaper.run())
        self.assertAlmostEqual(16.2, accum.getMeans()['X'])

    def testEquation(self):
        stepSize = 0.01
        endTime = 0.02001
        model = DimerModel()
        myLeaper = TauLeaper(model, stepSize, endTime)

        accum = MeanAccumulator()
        nRuns = pow(10, 5)
        for i in range(0, nRuns):
            accum.add(myLeaper.run())
        means = accum.getMeans()
        print('')
        for key in sorted(means.keys()):
            print("{0}: {1}".format(key, means[key]))
        print(numpy.mean(myLeaper.propensities))
