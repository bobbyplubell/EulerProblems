import math

def triangle(n):
    i = 0
    triangle = 0
    while i < n:
        triangle += i
        yield triangle
        i += 1

def divisors(n):
    divs = 0
    i = 1
    while i < math.sqrt(n):
        if(n % i == 0):
            divs += 1
            if(i != (n / i)):
                divs += 1
        i += 1
    return divs

def find_tri_with_divs(amtdivs, limit):
    i = 0
    tri = triangle(limit)
    while i < limit:
        newtri = tri.next()
        if(divisors(newtri) > amtdivs):
            return newtri
        i += 1

print(find_tri_with_divs(500, 100000))
