#Task-03
#Author Aditi Saha Ria
#ID : 20101238

class RealNumber:

    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def ping(self):
        print('I am in RealNumber class')
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    def __init__(self, a=1.0, b=1.0):
        super().__init__(a)
        self.imaginaryNumber = b
        self.realNumber = super().__str__()
        self.imaginaryNumber = f'ImaginaryPart: {float(self.imaginaryNumber)}'

    def __str__(self):
        return f'''{self.realNumber}
{self.imaginaryNumber}'''



cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)
print('---------')