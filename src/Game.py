import numpy as np
from Player import Player


class ISM:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.end = False
        self.p1 = Player()

    def printBoard(self):
        print(self.board)

    def getTable(self):
        s = []
        for i in range(3):
            for j in range(3):
                s.append(self.board[i, j])
        return np.reshape(s,(9,1))

    def updateState(self, action):
        reward = 0
        count = 0
        s = self.getTable()
        if not self.end:
            s[action] = 1
            for i in range(3):
                for j in range(3):
                    self.board[i, j] = s[count]
                    count += 1
            reward = self.win()
        if not self.end:
            action = np.random.randint(9)
            while not (s[action] == 0):
                action = np.random.randint(9)
            s[action] = -1
            count = 0
            for i in range(3):
                for j in range(3):
                    self.board[i, j] = s[count]
                    count += 1
            reward = self.win()
        return reward

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i, j] = 0
        self.end = False

    def train(self):
        reward = 0.0
        for i in range(2000):
            self.reset()
            while self.end == False:
                cur = self.getTable()
                action = self.p1.chooseAction(self.getTable())
                reward = self.updateState(action)
                next = self.getTable()
                self.p1.addReplaySet((cur,
                                      np.reshape(action,(1,1)), next, reward, self.end))
                self.p1.update(10)
                print("round", i)
            self.p1.reduceExp()

    def fun(self):
        reward = 0.0
        expReward = 0.0
        wins = 0.0
        losses = 0.0
        ties = 0.0
        for i in range(100):
            self.reset()
            while self.end == False:
                action = self.p1.chooseAction(self.getTable())
                reward = self.updateState(action)
            expReward = expReward+reward
            if(reward == 0):
                ties += 1
            if(reward == 1):
                wins += 1
            if(reward == -1):
                losses += 1
        print("Wins ", wins)
        print("Ties ", ties)
        print("Losses ", losses)
        print("Win Rate: ", expReward/100)

    def win(self):
        one = 0
        two = 0
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    one += 1
                elif self.board[i, j] == -1:
                    two += 1
            if one == 3:
                self.end = True
                return 1
            elif two == 3:
                self.end = True
                return -1
            else:
                one = 0
                two = 0
        for i in range(3):
            for j in range(3):
                if self.board[j, i] == 1:
                    one += 1
                elif self.board[j, i] == -1:
                    two += 1
            if one == 3:
                self.end = True
                return 1
            elif two == 3:
                self.end = True
                return -1
            else:
                one = 0
                two = 0
        for i in range(3):
            if self.board[i, i] == 1:
                one += 1
            elif self.board[i, i] == -1:
                two += 1
        if one == 3:
            self.end = True
            return 1
        elif two == 3:
            self.end = True
            return -1
        else:
            one = 0
            two = 0
        for i in range(3):
            if self.board[2-i, i] == 1:
                one += 1
            elif self.board[2-i, i] == -1:
                two += 1
        if one == 3:
            self.end = True
            return 1
        elif two == 3:
            self.end = True
            return -1
        else:
            one = 0
            two = 0
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == -1 or self.board[i, j] == 1:
                    count += 1
        if count == 9:
            self.end = True
            return 0
        return 0
