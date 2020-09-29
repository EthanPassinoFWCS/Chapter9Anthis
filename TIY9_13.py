from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for x in range(1, 11):
            print(f"Rolled a: {randint(1, self.sides)}")

d1 = Die()
d1.roll_die()
d2 = Die(10)
d2.roll_die()
d3 = Die(20)
d3.roll_die()
