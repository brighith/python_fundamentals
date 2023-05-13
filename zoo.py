

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal_name):
        self.animals.append(animal_name)
        return self

    def print_all_animals(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal():
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed_animal(self):
        self.health_level += 20
        self.happiness_level += 15
        return self


class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)

    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level , {self.happiness_level} happiness level! ")
        return self

    def feed_animal(self):
        self.health_level += 35
        self.happiness_level += 25
        return self


class Tiger(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)

    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level ,  {self.happiness_level} happiness level!")
        return self

    def feed_animal(self):
        super().feed_animal()
        return self


class Bears(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)

    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level ,  {self.happiness_level} happiness level!")
        return self

    def feed_animal(self):
        super().feed_animal()
        return self


z1 = Zoo("Yousef's Zoo")

simba = Lion("Simba", 5, 100, 100)
z1.add_animal(simba)
simba.feed_animal().feed_animal().feed_animal()

shere_khan = Tiger("Shere Khan", 2, 30, 30)
z1.add_animal(shere_khan)
shere_khan.feed_animal().feed_animal().feed_animal(
).feed_animal().feed_animal().feed_animal().feed_animal()

panda = Bears("Panda", 3, 50, 50)
z1.add_animal(panda)
panda.feed_animal().feed_animal().feed_animal().feed_animal()


z1.print_all_animals()
