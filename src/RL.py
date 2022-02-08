import numpy as np
import tensorflow as tf


class RL:
    def __init__(self):
        self.replaySet = []
        self.gamma = .99
        self.alpha = .8
        # tf.keras.backend.set_floatx('float64')
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(20, activation='relu', input_shape=(10,)),
            tf.keras.layers.Dense(20, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        loss_fn = tf.keras.losses.MeanSquaredError()
        self.model.compile(optimizer='adam',
                           loss=loss_fn,
                           metrics=[tf.keras.metrics.MeanSquaredError()])

    def randomAction(self, state):
        rand = np.random.randint(9)
        while(state[rand] != 0):
            rand = np.random.randint(9)
        return rand

    def updateReplaySet(self, set):
        size = len(self.replaySet)
        if size > 1000:
            self.replaySet.pop(0)
        self.replaySet.append(set)

    def gradientDescent(self, s, a, y):
        self.model.fit([s, a], y, epochs=1)

    def updateParameters(self, n):
        rand = np.random.randint(0, len(self.replaySet), n)
        y = np.zeros((n, 1))
        x = []
        for i in range(n):
            (cur, action, next, reward, terminal) = self.replaySet[rand[i]]
            v = np.vstack((cur, action))
            if i == 0:
                x = v.T
            else:
                x = np.vstack((x, v.T))

            (value, act) = self.getBestAction(next)
            if(terminal == True):
                y[i] = (reward)
            else:
                y[i] = self.alpha * (reward + self.gamma * value) + \
                    (1-self.alpha) * self.model(v.T)
        self.model.fit(x=x, y=y, epochs=1, verbose=0)

    def getBestAction(self, s):
        mx = np.NINF
        bestA = -1
        for act in range(9):
            # evaluate nn at each possible action
            v = np.vstack((s, act))
            res = self.model(v.T)
            m = np.asscalar(res.numpy())
            if(m > mx):
                mx = m
                bestA = act

        return mx, bestA 
