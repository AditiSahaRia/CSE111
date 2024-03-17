class Calculator:
    def __init__(self):
        print("Let’s Calculate!")

    def add(self, a, b):
        sum = a+b
        print(f'Value 1: {a}')
        print(f'Operator: +')
        print(f'Value 2: {b}')
        print(f'Result: {sum}')
    def subtract(self, a, b):
        sub = a-b
        print(f'Value 1: {a}')
        print(f'Operator: -')
        print(f'Value 2: {b}')
        print(f'Result: {sub}')
    def multiply(self, a, b):
        mul = a*b
        print(f'Value 1: {a}')
        print(f'Operator: *')
        print(f'Value 2: {b}')
        print(f'Result: {mul}')
    def divide(self, a, b):
        div = a/b
        print(f'Value 1: {a}')
        print(f'Operator: /')
        print(f'Value 2: {b}')
        print(f'Result: {div}')

obj1 = Calculator()
first_value = int(input())
operator = input()
second_value = int(input())
if operator=='+':
    obj1.add(first_value, second_value)
elif operator == '-':
    obj1.subtract(first_value, second_value)
elif operator == '*':
    obj1.multiply(first_value, second_value)
else:
    obj1.divide(first_value, second_value)