class Dates:
    def __init__(self, info):
        self.info = info

    @classmethod
    def toDashDate(cls, doc):
        frst, scnd, third = doc.split('/')
        obj1 = frst+'-'+scnd+'-'+third
        obj = Dates(obj1)
        return obj

    def getDate(self):
        return self.info


date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if(date1.getDate() == date2.getDate() ):
    print("Equal")
else:
    print("Unequal")

print()

print('Ans of subtask 5:')
print('''In the if else statement we check whether date1 and date2 has same parameter or not. We can see that the given
parameters are not same but before the if else statement we used method for date2 which replaced "/" this with
"-". So when we compare date1 and date2 if statement finds the ASCII value of each character of the parameters  
of date1 and date2 same according to their order. That's why the we get the output "equal".
''')