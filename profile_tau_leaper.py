import cProfile
import numpy
from tau_leaper import TauLeaper
from birth_model import BirthModel
from mean_accumulator import MeanAccumulator


def runTauLeaper():
    stepSize = 0.001
    endTime = 5
    model = BirthModel()
    myLeaper = TauLeaper(model, stepSize, endTime)

    accum = MeanAccumulator()
    nRuns = 100
    numpy.random.seed(0)
    for i in range(0, nRuns):
        accum.add(myLeaper.run())

cProfile.run('runTauLeaper()', sort='tottime')
