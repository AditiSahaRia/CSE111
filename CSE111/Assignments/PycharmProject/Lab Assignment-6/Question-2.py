class Customer:
    def __init__(self, name):
        self.name = name
    def greet(self, name=None):
        if name != None:
            print(f'Hello {name}!')
        else:
            print('Hello!')
    def purchase(self, *items):
        print(f'{self.name}, you purchased {len(items)} item(s):')
        for i in items:
            print(i)

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")