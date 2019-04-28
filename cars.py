class Car:

    max_speed = 500

    def __init__(self, brand):
        self.brand = brand

    def top_speed(self, speed):
        """Generates maximum speed in the race"""
        speed = randrange(0, max_speed)

class Porsche(Car):
    max_speed = 319
    def top_speed(self):
        self.top_speed

class Bugatti(Car):
    max_speed = 408
    def top_speed(self):
        self.top_speed

    """Which car is faster"""
while True:
    Porsche.max_speed > Bugatti.max_speed
    print('Porsche: {}'.format(Porsche.top_speed))
    print('Porsche won')
    break

    Bugatti.max_speed > Porsche.max_speed
    print('Bugatti: {}'.format(Bugatti.top_speed))
    print('Bugatti won')
    break