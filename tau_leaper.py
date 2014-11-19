import numpy as np


class TauLeaper:
    propensities = []

    def __init__(self, model, stepSize, endTime):
        self._model = model
        self._stepSize = stepSize
        self._endTime = endTime
        self._state = {}

    def run(self):
        time = self._stepSize
        self._state = self._model.getInitialState()
        while time < self._endTime:
            time += self._stepSize
            self._stepForward()
            # only append after the first step
        a = self._model.actions[0].getPropensity(self._state)
        self.propensities.append(a)
        return dict(self._state)

    def _stepForward(self):
        changeInAmounts = {k: 0 for k in self._state}
        for action in self._model.actions:
            propensity = action.getPropensity(self._state)
            nEvents = np.random.poisson(propensity*self._stepSize)
            for molecule, stoich in action.getNetStoich().items():
                changeInAmounts[molecule] += stoich*nEvents
        for molecule in changeInAmounts:
            self._state[molecule] += changeInAmounts[molecule]
