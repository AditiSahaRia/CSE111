#Question-03

#Name : Aditi Saha Ria
#ID : 20101238
#Section : 07
#Course Code : CSE111

class Player:
    def __init__(self,name,goalsScored,tacklesWon):
        self.name = name
        self.goalsScored = goalsScored
        self.tacklesWon = tacklesWon
        self.point=0
    def calculatePoint(self):
        self.point+=(self.goalsScored*4)+(self.tacklesWon*3)


class Attacker(Player):
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        super().__init__(self.name, self.a, self.b)
        print(f'Name: {self.name} ,Rating: {self.c}')
    def calculatePoint(self):
        super().calculatePoint()
        self.point += self.c*2
        print(f'Point of  {self.name} : {self.point}')


class Defender(Player):
    def __init__(self, name, a, b, c):
        self.name = name
        self.d = a
        self.e = b
        self.f = c
        super().__init__(self.name, self.d, self.e)
        print(f'Name: {self.name} ,Rating: {self.f}')
    def calculatePoint(self):
        super().calculatePoint()
        self.point += self.f*2
        print(f'Point of  {self.name} : {self.point}')



print('=========================')
p1 = Defender("Thiago Silva",5,12,8.5)
print('=========================')
p2 = Attacker("Cristiano Ronaldo",14,5,9.0)
print('=========================')
p3 = Attacker("Lionel Messi",12,9,9.5)
print('=========================')
p1.calculatePoint()
print('=========================')
p2.calculatePoint()
print('=========================')
p3.calculatePoint()
