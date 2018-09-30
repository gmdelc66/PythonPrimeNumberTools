from math import sqrt
def factorize(myNumber, checkPowers = True):

  # All the comments will be translated to English in the near future
  
  # Kommer att innehålla primfaktorerna till myNumber
  # Om powers = True, så innehåller den alla förekomster
  # av respektive enskild faktor (fullständig faktorisering).
  # Om powers = False finns enbart respektive unik primfaktor
  # med en gång oavsett antal förekomster.
  primeFactors = []


  # Kolla först trivialiteter, samt om talet faktiskt är ett primtal
    
  if myNumber < 2:
    print("Bad input")
    return []
      
  if (myNumber == 2 or myNumber == 3):
    primeFactors.append(myNumber)
    return primeFactors
  elif isPrime(myNumber):
    primeFactors.append(myNumber)
    return primeFactors

  # Loopen som letar efter delare
  for i in range(2, int(myNumber / 2) + 1):
        
    # Bara för att det är en delare behöver det inte vara en primfaktor...
    if myNumber % i == 0:
      if isPrime(i):
        # Om sant, i är en primfaktor till myNumber...
        primeFactors.append(i) # ...och ska läggas till i primeFactors.
            
      # Körs enbart om vi ska kolla efter mulipler av en och samma primfaktor
      if(checkPowers):
        # Nu måste vi kolla om det finns flera lika faktorer.
        # Det görs genom att testa om i^n (med ökande n) är 
        # jämnt delbart med det talet som faktorisera.
            
        n = 1 # n håller reda på vilken potens som primtalet förekom i
              # (t ex 24 = 2^3 * 3^1)
            
        # Loopen kollar om det aktuella talet...
        while (i ** n) <= int(myNumber / 2) + 1:
          n += 1
          if myNumber % i ** n == 0:
                    
            if isPrime(i):
              # Ja, samma i som ovan förekommer en gång till i primtalsuppdelningen
              primeFactors.append(i)
                    
            # Fortsätt loopa för att ev. hitta flera potenser av ett och samma i i talet
        # Ett värde på i är nu behandlat...
    # ...gå vidare till nästa.
        
  return primeFactors
  
# En funktion som genererar primtal mellan två värden
def genPrimesBetween(lower, upper):
  primeNumbers = []
  for number in range(lower, upper + 1):
    if isPrime(number):
      primeNumbers.append(number)
  return primeNumbers

# En funktion som genererar de n första primtalen
def genFirstPrimes(number):
  primeList = [2]
  numberOfPrimes = 1
  while numberOfPrimes < number:
    primeList.append(nextPrime(primeList[-1]))
    numberOfPrimes += 1
  return primeList

# En funktion som returnerar primtalet efter det givna talet
def nextPrime(number):
  number += 1
  while not isPrime(number):
    number += 1
  return number

# En funktion som returnerar primtalet före det givna talet
def prevPrime(number):
  if number > 2:
    number -= 1
  while not isPrime(number):
    number -=1
  return number

# Denna funktion avgör om ett tal är ett primtal
def isPrime(number):

  if (number < 2):
    return False
    
  if (number <= 3):
    return True
    
  i = 2
  while i <= sqrt(number):
    if (number % i) == 0:
      return False
    i += 1

  return True

# Denna funktion avgör om två tal är relativt prima
def isRelPrime(a, b):
  if gcd(a,b) > 1:
    return False
  return True

# Denna funktion returnerar största gemensamma delare till två tal
def gcd(a, b):
  if a % b != 0:
    return gcd(b, a % b)
  else:
    return b

# Denna funktion returnerar minsta gemensamma nämnare till två tal
def lcd(a, b):
  return(a * b // gcd(a, b))
