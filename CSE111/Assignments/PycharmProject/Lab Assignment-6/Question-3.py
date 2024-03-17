class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def sleep(self, time=None):
        if time != None and time <= 5:
            return f'{self.name} sleeps {time} hours daily and should have Mixed Veggies'
        elif time != None and time <= 8:
            return f'{self.name} sleeps {time} hours daily and should have Eggplant & Tofu'
        elif time != None and time <= 11:
            return f'{self.name} sleeps {time} hours daily and should have Broccoli Chicken'
        elif time == None:
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"


panda1 = Panda("Kunfu","Male", 5)
panda2 = Panda("Pan Pan","Female",3)
panda3 = Panda("Ming Ming","Female",8)
print(f"{panda1.name} is a {panda1.gender} Panda Bear who is {panda1.age} years old")
print(f"{panda2.name} is a {panda2.gender} Panda Bear who is {panda2.age} years old")
print(f"{panda3.name} is a {panda3.gender} Panda Bear who is {panda3.age} years old")
print()
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())