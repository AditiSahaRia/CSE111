class Circle:
    pi = 3.141592653589793
    def __init__(self, radius):
        self.__radius = radius
        self.__area = 0
        self.__total = 0

    def area(self):
        self.__area = self.__radius*self.__radius*Circle.pi
        return self.__area

    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius

    def __add__(self, other):
        new_radius = self.__radius+other.__radius
        obj = Circle(new_radius)
        return obj

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())