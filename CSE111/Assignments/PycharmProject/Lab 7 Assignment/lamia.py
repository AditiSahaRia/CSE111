class animal:
    def pet(self):
        return self.wild()
    def wild(self):
        return 'Tiger'

class arthropodos(animal):
    def wild(self):
        return 'butterfly'

obj1 = animal()
obj2 = arthropodos()
print(obj1.wild(), obj2.wild())