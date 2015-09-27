
amt = 0
infile = open("nums.txt", "r")
for line in infile:
    amt += int(line)
    print(amt)

print(amt)
