__author__ = 'Brutus'


# Opis parametrów roweru
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

f = open("input.txt", "r")

for line in f.readlines():
    print(line.split())
