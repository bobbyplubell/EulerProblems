import bobmath

abundants = bobmath.get_abundants(28123)
print(abundants)

def get_abundant_summables(limit):
    global abundants
    summable = []
    i = 0
    while i < len(abundants):
        z = i
        while z < len(abundants):
            summable.append(i+z)
    return summable

if __name__ == "__main__":
    summy = 0
    summables = get_abundant_summables(28123)
    for i in xrange(28123):
        if not i in summables:
            summy += i
            print(summy)

    print(summy)
