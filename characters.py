import random

class Character:

    def __init__(self, HP, DP, SP):
        self.HP = HP
        self.DP = DP
        self.SP = SP


    def dice(self):
        return random.randint(1, 6)


    def area(self): # count = 0 loop!
        count = 0
        for x in range(1, 100):
            count += 1
            return count

    def level(self):
        prob = random.randint(1, 10)
        if prob <= 5:
            return self.area()
        elif prob <= 5 and prob <= 10:
            return self.area() + 1
        elif prob == 10:
            return self.area() + 2

    def strike(self):
        SV = (self.SP + self.dice()) * 2
        return SV








