import bobmath

def primes_quad(a, b):
    primes = 0
    n = 0
    num = (n * n) + (a * n) + b
    while bobmath.is_prime(num):
        primes += 1
        num = (n * n) + (a * n) + b
        n += 1
    return primes

if __name__ == "__main__":
    most_primes = 0
    a_most = 0
    b_most = 0
    for a in xrange(-1001, 1001):
        for b in xrange(-1001, 1001):
            primes = primes_quad(a,b)
            if primes > most_primes:
                print("New Largest: " + str(primes) + " a: "\
 + str(a) + " b: " + str(b))
                most_primes = primes
                a_most = a
                b_most = b

    print(str(a_most) + " " + str(b_most))
    print(a_most*b_most)
