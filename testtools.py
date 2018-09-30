# Importerar funktionerna
# - factorize(n) // Returnerar en lista på alla primfaktorer i n
# - genPrimesBetween(a, b) // Returnerar en lista med alla primtal mellan, och inklusive, a och b
# - genFirstPrimes(n) // Returnerar en lista med de n första primtalen
# - nextPrime(n)  // Returnerar första talet som är större än n, och är ett primtal
# - prevPrime(n) // Returnerar första talet som är mindre än n, och är ett primtal
# - isPrime(n) // Är talet ett primtal? Returnerar True eller False
# - isRelPrime(a, b) // Har talen gemensamma primfaktorer? Returnerar True eller False
# - gcd(a, b)  // Största gemensamma delare
# - lcd(a, b) // Minsta gemensamma nämnare

from primetools import *
from random import randint

print("Demonstration av funktionerna i primetools\n")

myRandomNumber1 = randint(1000, 10000)
myRandomNumber2 = randint(1000, 10000)
print("Två framslumpade heltal mellan 1 000 och 10 000:")
print("Tal 1:", myRandomNumber1)
print("Tal 2:", myRandomNumber2)
print()
print("Faktoriserar dessa:")
print("Primfaktorer i Tal 1:", factorize(myRandomNumber1))
print("Primfaktorer i Tal 2:", factorize(myRandomNumber2))
print()
print("Kontrollerar om något av dessa tal är ett primtal:")
print("Kollar Tal 1:", isPrime(myRandomNumber1))
print("Kollar Tal 2:", isPrime(myRandomNumber2))
print()
print("Kollar om Tal 1 och Tal 2 är relativt prima:", isRelPrime(myRandomNumber1, myRandomNumber2))
print()
print("Beräknar största gemensamma delare till Tal 1 och Tal 2:")
print("SGD =", gcd(myRandomNumber1, myRandomNumber2))
print()
print("Beräknar minsta gemensamma nämnare till Tal 1 och Tal 2")
print("MGN =", lcd(myRandomNumber1, myRandomNumber2))
print()
print("Första primtal som är större än Tal 1:", nextPrime(myRandomNumber1))
print("Första primtal som är mindre än Tal 1:", prevPrime(myRandomNumber1))
print()
print("Antal primtal upp t.o.m Tal 1:")
primes = genPrimesBetween(2, myRandomNumber1)
print(len(primes))
print()
print("Varav de tre sista är:")
prime3Last = [primes[-3], primes[-2], primes[-1]]
print(prime3Last)
