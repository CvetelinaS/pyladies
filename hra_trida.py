
from random import randrange

class Robot():
    def __init__(self, lifes)
        self.lifes = lifes

class Aggressive(Robot):
    def attack(self, robot):
        damage = randrange(0, 11)
        robot.take_damage(damage)

    def take_damage(self, damage):
        if self.lifes - damage < 0:
            self.lifes = 0
        else:
            self.lifes -= damage