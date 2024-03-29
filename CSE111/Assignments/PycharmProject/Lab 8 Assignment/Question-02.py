#Task-02
#Author Aditi Saha Ria
#ID : 20101238

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y+=1
    def moveDown(self):
        self.y-=1
    def moveRight(self):
        self.x+=1
    def moveLeft(self):
        self.x-=1
    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'

class Vehicle2010(Vehicle):
    result = False
    def __init__(self):
        super().__init__()

    def moveUpperRight(self):
        super().moveUp()
        super().moveRight()

    def moveUpperLeft(self):
        super().moveUp()
        super().moveLeft()
    def moveLowerRight(self):
        super().moveDown()
        super().moveRight()
    def moveLowerLeft(self):
        super().moveDown()
        super().moveLeft()
    def equals(self, other):
        count = 0
        if self.x == other.x:
            count += 1
        if self.y == other.y:
            count += 1
        if count == 2:
            Vehicle2010.result = True
        else:
            Vehicle2010.result = False
        return Vehicle2010.result

print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))
print('------')