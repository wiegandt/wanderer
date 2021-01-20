from characters import Character

class Skeleton(Character):

    def __init__(self, HP, DP, SP): #area
        super().__init__(HP, DP, SP)
        self.HP = 2 * self.level() * self.dice()
        self.DP = (self.level() / 2) + self.dice()
        self.SP = self.level() * self.dice()
        self.skeleton = [] # goes in main

        self.x = 0
        self.y = 0


