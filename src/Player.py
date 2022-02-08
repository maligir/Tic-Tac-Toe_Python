from RL import RL
import numpy as np
from RL import RL
from array import *


class Player:
    def __init__(self):
        self.RL = RL()
        self.exp = 1
    # choose action based on exp

    def chooseAction(self, state):
        # chooses random action

        if(np.random.rand() < self.exp):
            return self.RL.randomAction(state)
        else:
            # choose action with RL
            (mx, action) = self.RL.getBestAction(state)
            return action

    def addReplaySet(self, set):
        self.RL.updateReplaySet(set)
    # reduces exp

    def reduceExp(self):
        self.exp = max([.05, .997*self.exp])
    # updates parameters

    def update(self, n):
        self.RL.updateParameters(n)
