class Action:
    def __init__(self, rateConstant, reactants, products):
        allStoich = list(reactants.items()) + list(products.items())
        for molecule, stoich in allStoich:
            if stoich <= 0 or stoich > 2:
                message = "Invalid stoichiometry for {0}: {1}".\
                          format(molecule, stoich)
                raise Exception(message)
        self._rateConstant = rateConstant
        self._reactants = reactants
        self._products = products
        self._netStoich = self._initializeNetStoich()

    def getPropensity(self, state):
        propensity = self._rateConstant
        for reactant, stoich in self._reactants.items():
            propensity *= _comb(state[reactant], stoich)
        return propensity

    def getNetStoich(self):
        return self._netStoich

    def _initializeNetStoich(self):
        netStoich = {k: -1*v for k, v in self._reactants.items()}
        for product, stoich in self._products.items():
            if product in netStoich:
                netStoich[product] += stoich
            else:
                netStoich[product] = stoich
        return netStoich


def _comb(amount, stoich):
    if(stoich == 1):
        return amount
    elif stoich == 2:
        return amount*(amount-1)*0.5
    raise Exception("Invalid stoichiometry: {0}".format(stoich))
