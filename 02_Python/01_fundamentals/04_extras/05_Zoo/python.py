class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def show_info(self):
        print(f"\nName:{self.name}\nHealth: {self.health}\nHappiness:{self.happiness}")

    def feed(self):
        self.health +=10
        self.happiness +=10

class squirrel(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 50
        self.happiness = 50

    def feed(self):
        self.health +=5
        self.happiness +=5


class bear(Animal):
    def __init__(self, name, age, col):
        super().__init__(name, age)
        self.color = col
        self.health = 75
        self.happiness = 75


    def feed(self):
        self.health +=15
        self.happiness +=15


class lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 90
        self.happiness = 90


    def feed(self):
        self.health +=20
        self.happiness +=20


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_lion(self, name, age):
        self.animals.append( lion(name,age) )
    
    def add_bear(self, name, age, col):
        self.animals.append( bear(name, age, col) )

    def add_squirrel(self, name, age):
        self.animals.append( squirrel(name, age) )    
    
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.show_info()




zoo1 = Zoo("El zoo de John")
zoo1.add_lion("Nala",10)
zoo1.add_lion("Simba",10)
zoo1.add_bear("Rajah", 15, "brown")
zoo1.add_squirrel("Mota", 16)
zoo1.print_all_info()



# ani1= squirrel("Mota", 16)
# ani1.show_info()
# ani1.feed()
# ani1.show_info()
