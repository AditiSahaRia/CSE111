#Task-06
#Author Aditi Saha Ria
#ID : 20101238

class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin

class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)

class Mango(Fruit):
    def __init__(self, formalin=True, name='Mango'):
        self.formalin = formalin
        self.name = name
        super().__init__(self.formalin, self.name)

    def __str__(self):
        return 'Mangos are bad for you'

class Jackfruit(Fruit):
    def __init__(self, formalin=False, name='Jackfruit'):
        self.formalin = formalin
        self.name = name
        super().__init__(self.formalin, self.name)

    def __str__(self):
        return 'Jackfruits are good for you'

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)