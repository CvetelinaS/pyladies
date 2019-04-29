from random import randrange
"""create a class"""
class Car:

    max_speed = 500

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        """Generates maximum speed in the race"""
        speed = randrange(0, self.max_speed)
"""inheriting classes"""
class Porsche(Car):
    max_speed = 319
    def go(self, speed):
        self.max_speed

class Bugatti(Car):
    max_speed = 408
    def go(self, speed):
        self.max_speed

    """Which car would be faster"""
while True:
    if Porsche.max_speed > Bugatti.max_speed:
        print('Porsche: {}'.format(Porsche.max_speed))
        print('Porsche won')
    if Bugatti.max_speed > Porsche.max_speed:
        print('Bugatti: {}'.format(Bugatti.max_speed))
        print('Bugatti won')
        break