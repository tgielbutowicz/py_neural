__author__ = 'Brutus'
import math

class Perceptron:
    def __init__(self, weights, activationTreshold):
        self.weights = weights
        self.activationTreshold = activationTreshold

    def sigmoidelFunction(x, alfa = 1):
        1.0 / (1.0 + math.pow(math.e,-x*alfa))