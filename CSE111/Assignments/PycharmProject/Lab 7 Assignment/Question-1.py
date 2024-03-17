class Student:
    ID = 0
    def __init__(self, name, department, age, cgpa):
        self.name = name
        self.dept = department
        self.age = age
        self.cg = cgpa
        Student.ID += 1

    def get_details(self):
        print(f'ID: {Student.ID}')
        print(f'Name: {self.name}')
        print(f'Department: {self.dept}')
        print(f'Age: {self.age}')
        print(f'CGPA: {self.cg}')

    @classmethod
    def from_String(cls, info):
        name, department, age, cgpa = info.split('-')
        obj = cls(name, department, age, cgpa)
        return obj

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

print("-----------------------")

print('''Ans of subtask 5:
Class variable changes for all objects and the output is same for all the objects but instance variable
changes with the reference of a particular object and the output is not same for all the objects.
''')


print("-----------------------")

print('''Ans of subtask 6:
Class method can be called with the reference of an individual object or by the class itself whereas instance method
can only be called with the reference of an individual object. Furthermore, when wee need change any document for the
whole class it cannot be achieved with a instance method but this problem can be easily done by using class method.  
''')