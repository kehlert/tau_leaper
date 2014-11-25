import unittest
from stat_accumulator import StatAccumulator


class TestConstructor(unittest.TestCase):
    def testConstructor(self):
        StatAccumulator()

    def testGetMean(self):
        accum = StatAccumulator()
        accum.add({'X': 5, 'Y': -1})
        accum.add({'X': 6, 'Y': 4})
        accum.add({'X': 1, 'Y': 0})
        self.assertDictEqual({'X': 4, 'Y': 1}, accum.getMeans())

    def testGetVar(self):
        accum = StatAccumulator()
        accum.add({'X': 5, 'Y': -1})
        accum.add({'X': 6, 'Y': 4})
        accum.add({'X': 1, 'Y': 6})
        self.assertDictEqual({'X': 7, 'Y': 13}, accum.getVars())
