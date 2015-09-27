import bobmath

def amicables(limit):
    amics = []
    i = 0
    while i < limit:
        asum = sum(bobmath.get_divisors(i))
        bsum = sum(bobmath.get_divisors(asum))
        if(bsum == i and i != asum):
            amics.append(i)
            if not bsum in amics:
                amics.append(bsum)
        i += 1
    return amics

def is_amicable(n):
    asum = sum(bobmath.get_divisors(n))
    bsum = sum(bobmath.get_divisors(asum))
    if(bsum == n):
        return True
    else:
        return False

amics = amicables(10000)
print(sum(amics))
