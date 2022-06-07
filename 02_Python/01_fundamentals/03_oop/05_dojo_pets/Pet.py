class Pet:
    def __init__(self, name, type, food):
        self.name = name
        self.type = type
        self.food = food
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health +=5


class Dog(Pet):
    def __init__(self, name, type, food):
        super().__init__(name, type, food)

    def sound(self):
        print("woof")


class Cat(Pet):
    def __init__(self, name, type, food):
        super().__init__(name, type, food)

    def sound(self):
        print("miau")