from random import randint

class flea():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        dir = randint(0,3)
        if(dir == 0 and self.y < 30):
            self.y += 1
        elif(dir == 1 and self.y > 0):
            self.y -= 1
        elif(dir == 2 and self.x < 30):
            self.x += 1
        elif(dir == 3 and self.x > 0):
            self.x -= 1
        else:
            self.jump()
