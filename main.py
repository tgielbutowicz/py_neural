__author__ = 'Brutus'
import random
import numpy
import perceptron

# Opis parametrów roweru
# nazwa
# wynik
# 1. liczba kol
# 2. opona slick
# 3. opona semi-slick
# 4. opona terenowa
# 5. rozmiar kola
# 6. skok widelca
# 7. amortyzator
# 8. pozycja sportowa
# 9. pozycja rekreacyjna
# 10. hamulce

activationTreshold = 0.9
errors = []
eta = 0.04
n = 5000

f = open("input.txt", "r")
training_data = []
expected = []

for line in f.readlines():
    line_split = line.split()
    training_data.append(line_split[1:])
per = perceptron.Perceptron([random.random() for _ in range(0, 10)],activationTreshold)

for i in range(n):
    row_of_data = random.choice(training_data)
    expected = int(row_of_data[0])
    properties = numpy.array(row_of_data[1:],dtype=float)
    result = numpy.dot(per.weights, properties)
    error = expected - per.sigmoidelfun(result)
    errors.append(error)
    per.weights += eta * error * properties

for x in training_data:
    properties = numpy.array(x[1:],dtype=float)
    result = per.sigmoidelfun(numpy.dot(properties, per.weights))
    print("{}: {} -> {}".format(x, result, per.unit_step(result)))
    #print(errors)

#from pylab import plot, ylim
import matplotlib.pylab
matplotlib.pylab
matplotlib.pylab.ylim([-1,1])
matplotlib.pylab.plot(errors)
matplotlib.pylab.show()




