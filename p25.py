def fibbonacci(n):
    last = 1
    sec_last = 0
    i = 1
    while i <= n:
        new = last + sec_last
        sec_last = last
        last = new
        i += 1
        yield new,i

def digits(n):
    return len(str(int(n)))

if __name__ == "__main__":
    f = fibbonacci(100000)
    num,i = f.next()
    while(digits(num) < 1000):
        num,i = f.next()

    print(str(i) + " " + str(num))
