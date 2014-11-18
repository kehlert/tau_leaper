import unittest
from action import Action


class TestConstructor(unittest.TestCase):
    def testBadReactantStoich(self):
        rateConstant = 0.1
        reactants = {'X': -1}
        with self.assertRaises(Exception):
            Action(rateConstant, reactants, {})

    def testInvalidStoich(self):
        rateConstant = 0.1
        reactants = {'X': 0}
        with self.assertRaises(Exception):
            Action(rateConstant, reactants, {})


class TestGetNetStoich(unittest.TestCase):
    def testGetNetStoich(self):
        rateConstant = 0.1
        reactants = {'X': 1, 'Y': 2}
        products = {'X': 2, 'Z': 1}
        myAction = Action(rateConstant, reactants, products)
        self.assertDictEqual({'X': 1, 'Y': -2, 'Z': 1}, myAction.getNetStoich())


class TestGetPropensity(unittest.TestCase):
    def testZerothOrder(self):
        state = {'X': 10}
        rateConstant = 0.1
        products = {'X': 1}
        myAction = Action(rateConstant, {}, products)
        self.assertEqual(0.1, myAction.getPropensity(state))

    def testFirstOrder(self):
        state = {'X': 10}
        rateConstant = 0.1
        reactants = {'X': 1}
        myAction = Action(rateConstant, reactants, {})
        self.assertEqual(1, myAction.getPropensity(state))

    def testSecondOrder(self):
        state = {'X': 10, 'Y': 5}
        rateConstant = 0.1
        reactants = {'X': 1, 'Y': 1}
        myAction = Action(rateConstant, reactants, {})
        self.assertEqual(5, myAction.getPropensity(state))

    def testAnotherSecondOrder(self):
        state = {'X': 10}
        rateConstant = 0.1
        reactants = {'X': 2}
        myAction = Action(rateConstant, reactants, {})
        self.assertEqual(4.5, myAction.getPropensity(state))

    def testWithProducts(self):
        state = {'X': 10, 'Y': 5}
        rateConstant = 0.1
        reactants = {'X': 1}
        products = {'Y': 1}
        myAction = Action(rateConstant, reactants, products)
        self.assertEqual(1, myAction.getPropensity(state))

    def testZeroAmount(self):
        state = {'X': 0}
        rateConstant = 0.1
        reactants = {'X': 1}
        myAction = Action(rateConstant, reactants, {})
        self.assertEqual(0, myAction.getPropensity(state))

    def testSameMoleculeReactantAndProduct(self):
        state = {'X': 10}
        rateConstant = 0.1
        reactants = {'X': 1}
        products = {'X': 2}
        myAction = Action(rateConstant, reactants, products)
        self.assertEqual(1, myAction.getPropensity(state))

    def testChangeState(self):
        state = {'X': 10}
        rateConstant = 0.1
        reactants = {'X': 1}
        myAction = Action(rateConstant, reactants, {})
        self.assertEqual(1, myAction.getPropensity(state))
