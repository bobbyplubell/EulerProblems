import math

def triangle(n):
    i = 0
    triangle = 0
    while i < n:
        triangle += i
        yield triangle
        i += 1

def amt_divisors(n):
    divs = 0
    i = 1
    while i < math.sqrt(n):
        if(n % i == 0):
            divs += 1
            if(i != (n / i)):
                divs += 1
        i += 1
    return divs

def get_divisors(n):
    divs = []
    i = 1
    while i < math.sqrt(n):
        if(n % i == 0 and i != n):
            divs.append(i)
            if(n != (n / i)):
               divs.append(n / i)
        i += 1
    return divs

def fact(n):
    fact = 1
    i = n
    while i > 0:
        fact *= i
        i -= 1

    return fact

def is_prime(n):
    i = 1
    if(round(math.sqrt(abs(n))) == math.sqrt(abs(n))):
        return False
    while i < math.sqrt(abs(n)):
        if(n % i == 0 and i != n and i != 1):
            return False
        i += 1
    return True

def get_abundants(limit):
    i = 1
    abundants = []
    while i < limit:
        if(sum(get_divisors(i)) > i):
            abundants.append(i)
        i += 1
    return abundants

def sum_digits(n):
    summy = 0
    string = str(int(n))
    for ch in string:
        summy += int(ch)
    return summy
