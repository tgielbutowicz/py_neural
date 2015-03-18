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
eta = 0.01
n = 2000

f = open("input.txt", "r")
bikes = []
expected = []

for line in f.readlines():
    line_splitted = line.split()
    bikes.append(line_splitted[1:])
per = perceptron.Perceptron([random.random() for _ in range(0, 10)],activationTreshold)

for i in range(n):
    bikec = random.choice(bikes)
    expected = int(bikec[0])
    bike = numpy.array(bikec[1:],dtype=float)
    result = numpy.dot(per.weights, bike)
    error = expected - per.sigmoidelfun(result)
    errors.append(error)
    per.weights += eta * error * bike

for x in bikes:
    bike = numpy.array(x[1:],dtype=float)
    result = numpy.dot(bike, per.weights)
    print("{}: {} -> {}".format(x[:2], result, per.unit_step(result)))
