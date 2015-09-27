import math

num = str(int(math.pow(2, 1000)))
sum = 0

for ch in num:
    sum += int(ch)

print(sum)
