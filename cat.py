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
