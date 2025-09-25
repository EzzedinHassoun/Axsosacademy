class Zoo:
    def __init__(self, zoo_name):

        self.animals = []
        self.name = zoo_name

    
    def add_lion(self ,name):
        lion = Lion(name)
        self.animals.append(lion)

    def add_Tiger(self, name):
        tiger = Tiger(name)
        self.animals.append(tiger)
    
    
    def add_Monkey(self ,name):

        monkey = Monkey(name)

        self.animals.append(monkey)
        
    
    def display_animals(self):

        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    
    def feed_all(self):
        for animal in self.animals:

            animal.feed()




class Animal:
    def __init__(self,name,age):

        self.name = name
        self.health_level = 100
        self.happiness_level =100

        self.age=age

    
    def display_info(self):
        print(f"Name: {self.name}")

        print(f"Health Level: {self.health_level}")
        print(f"Happiness Level: {self.happiness_level}")

        print(f"age: {self.age}")

    
    def feed(self):
        self.health_level +=10
        self.happiness_level += 10

        print(f"{self.name} Lion was fed.")
        print(f"{self.age}")





class Lion(Animal):

    def __init__(self, name ,age=2):
        super().__init__(name,age)

        self.health_level = 100
        self.happiness_level = 90

        self.age=2
    
    def feed(self):
        self.happiness_level += 15
        self.health_level += 10

        print(f"{self.name} was fed.")

    

class Monkey(Animal):

    def __init__(self, name, favourite_food = "Banana",age=3):

        super().__init__(name,age)
        self.favourite_food = favourite_food
        self.health_level = 80

        self.happiness_level = 80
    
    def feed(self):

        self.happiness_level += 20
        self.health_level += 10
        print(f"{self.name} Monkey was fed.")


class Tiger(Animal):

    def __init__(self, name,age=4):

        super().__init__(name,age)
        self.health_level = 85
        self.happiness_level = 85

    def feed(self):
        
        self.health_level += 10
        self.happiness_level += 10
        print(f"{self.name} Tiger was fed.")


zoo1 = Zoo("John's Zoo")

zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_Monkey("Tarazan")
zoo1.add_Tiger("Shere Khan")
zoo1.add_Tiger("Rajah")

zoo1.display_animals()
zoo1.feed_all()