from characters import Character

class Boss(Character):

    def __init__(self, HP, DP, SP):
        super().__init__(HP, DP, SP)
        self.HP = 2 * self.level() * self.dice() + self.dice()
        self.DP = (self.level() / 2) * self.dice() + self.dice() / 2
        self.SP = self.level() * self.dice() + self.level()

        self.x = 0
        self.y = 0
