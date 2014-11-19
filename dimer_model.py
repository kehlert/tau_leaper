from action import Action


class DimerModel:
    def __init__(self):
        self._initialState = {'X1': 40, 'X2': 20}
        self.actions = [Action(1,  {'X1': 2}, {'X2': 1}),
                        Action(10, {'X2': 1}, {'X1': 2})]

    def getInitialState(self):
        return dict(self._initialState)
