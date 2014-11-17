from scipy.misc import comb


class Action:
    def __init__(self, state, rateConstant, reactants, products):
        allStoich = list(reactants.items()) + list(products.items())
        for molecule, stoich in allStoich:
            if stoich <= 0:
                message = "Invalid stoichiometry for {0}: {1}".\
                          format(molecule, stoich)
                raise Exception(message)

        self._state = state
        self._rateConstant = rateConstant
        self._reactants = reactants
        self._products = products

    def getPropensity(self):
        propensity = self._rateConstant
        for reactant, stoich in self._reactants.items():
            propensity *= comb(self._state[reactant], stoich)
        return propensity

    def getNetStoich(self):
        netStoich = {k: -1*v for k,v in self._reactants.items()}
        for product, stoich in self._products.items():
            try:
                netStoich[product] += stoich
            except KeyError:
                netStoich[product] = stoich
        return netStoich
