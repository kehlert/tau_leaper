import numpy as np


class TauLeaper:
    def __init__(self, model, stepSize, endTime):
        self._model = model
        self._stepSize = stepSize
        self._endTime = endTime
        self._state = {}

    def run(self):
        time = self._stepSize
        self._state = self._model.getInitialState()
        while time < self._endTime:
            self._stepForward()
            time += self._stepSize
        return dict(self._state)

    def _stepForward(self):
        for action in self._model.actions:
            propensity = action.getPropensity(self._state)
            nEvents = np.random.poisson(propensity)
            for molecule, stoich in action.getNetStoich().items():
                self._state[molecule] += stoich*nEvents
