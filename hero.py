from characters import Character

class Hero(Character):

    def __init__(self, HP, DP, SP):
        super().__init__(HP, DP, SP)
        self.HP = 20 + 3 * self.dice()
        self.DP = 2 * self.dice()
        self.SP = 5 + self.dice()

        self.x = 0
        self.y = 0






