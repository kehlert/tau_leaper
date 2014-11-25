import unittest
import numpy
from tau_leaper import TauLeaper
from birth_model import BirthModel
from dimer_model import DimerModel
from stat_accumulator import StatAccumulator


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

        accum = StatAccumulator()
        nRuns = 10
        numpy.random.seed(0)
        for i in range(0, nRuns):
            accum.add(myLeaper.run())
        self.assertAlmostEqual(16.2, accum.getMeans()['X'])

    def testEquation(self):
        stepSize = 0.001
        # Specify the length of the sim in number of steps?
        # Might be able to speed up the inner loop by changing
        # the for loop, possibly into something very different.
        # Also try inlining the step forward function.
        endTime = 0.01001
        model = DimerModel()
        myLeaper = TauLeaper(model, stepSize, endTime)

        accum = StatAccumulator()
        nRuns = pow(10, 5)
        for i in range(0, nRuns):
            accum.add(myLeaper.run())
        means = accum.getMeans()
        variances = accum.getVars()
        print('')
        for key in sorted(means.keys()):
            print("{0}: mean: {1} | var: {2}".format(key,
                                                     means[key],
                                                     variances[key]))
        print(numpy.mean(myLeaper.propensities))
