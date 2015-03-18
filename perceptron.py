__author__ = 'Brutus'
import math

class Perceptron:
    def __init__(self, weights, activationTreshold):
        self.weights = weights
        self.activationTreshold = activationTreshold

    def sigmoidelfun(self,x, alfa = 1):
        return 1.0 / (1.0 + math.pow(math.e,-x*alfa))

    def unit_step(self,x):
        return 1 if x < self.activationTreshold else 0