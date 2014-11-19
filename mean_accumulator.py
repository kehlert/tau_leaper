import numpy


class MeanAccumulator:
    def __init__(self):
        self._data = {}

    def add(self, newData):
        for key, val in newData.items():
            if key not in self._data:
                self._data[key] = []
            self._data[key].append(val)

    def getMeans(self):
        means = {}
        for key in self._data:
            keyData = self._data[key]
            means[key] = numpy.mean(keyData)
        return means
