import unittest
from mean_accumulator import MeanAccumulator


class TestConstructor(unittest.TestCase):
    def testConstructor(self):
        MeanAccumulator()

    def testGetMean(self):
        accum = MeanAccumulator()
        accum.add({'X': 5, 'Y': -1})
        accum.add({'X': 6, 'Y': 4})
        accum.add({'X': 1, 'Y': 0})
        self.assertDictEqual({'X': 4, 'Y': 1}, accum.getMeans())
