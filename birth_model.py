from action import Action


class BirthModel:
    def __init__(self):
        self._initialState = {'X': 10}
        self.actions = [Action(self._initialState, 0.1, {'X': 1}, {'X': 2})]
