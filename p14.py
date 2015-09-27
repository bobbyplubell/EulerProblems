
paths = 0

def down((x,y)):
    y += 1
    return (x,y)

def right((x,y)):
    x += 1
    return (x,y)

def mutate((x,y)):
    if(y <= 20):
        mutate(down((x,y)))
    
    if(x <= 20):
        mutate(right((x,y))

    if(x == 20 and y == 20):
        paths += 1

mutate((0,0))
print(paths)
