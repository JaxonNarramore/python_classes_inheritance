# self is kinda the same thing as using .this in classes in React
# Classes are templates
# instinces are called objects

# Class

class Car():
    """ This is a car class that will display the make, model and color of the car """  # shows up in the help  function, show be describing what the class does or its purpose
    # self must always be the first paramter in the __init__ function

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100

    def __str__(self):
        # should have this with every __init__ to show what is in the class
        return '{}, {}, {}'.format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 10
        print('skrt skrt')
        print(self.gas)

    def fill_tank(self):
        self.gas = 100
        print('Car is now filled')

    def check_gas(self):
        print(f'Gas handle: {self.gas}')


car1 = Car('Tesla', 'S', 'Red')

# help(car1)
print(car1)
car1.drive()  # equal to 90
car1.drive()  # equal to 80
car1.check_gas()
car1.fill_tank()
car1.check_gas()


class Cat():
    def __init__(self, color, nice, fav_toy):
        self.color = color
        self.nice = nice
        self.fav_toy = fav_toy
        self.age = 1

    def __str__(self):
        return '{}, {}, {}'.format(self.color, self.nice, self.fav_toy)

    def birthday(self):
        self.age + 1
        print('Stella is now', self.age + 1)
        print('Happy birthday!')


stella = Cat('black and white', False, 'Chick-fl-a straw')
piper = Cat('white', True, 'hairtie')

print(stella)
print(piper)
stella.birthday()
