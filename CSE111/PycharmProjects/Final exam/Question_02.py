#Question-02

#Name : Aditi Saha Ria
#ID : 20101238
#Section : 07
#Course Code : CSE111

class Account:
    count = 0
    def __init__(self, name, age, ocptn, income):
        self.name = name
        self.age = age
        self.ocptn = ocptn
        self.income = income
        self.balance = 0
        Account.count += 1

    def addMoney(self, add):
        self.add = add
        self.balance = self.income+self.add

    def withdrawMoney(self, withdraw):
        self.withdraw = withdraw
        self.balance = self.income-self.withdraw

    def printDetails(self):
        if self.balance < 0:
            print('Not sufficient balance.')
        elif self.balance > self.income:
            print('Add Money successfully !!')
        elif self.balance < self.income:
            print('Withdraw Successful !!')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Occupation: {self.ocptn}')
        if self.balance>=0:
            print(f'Total Amount:  {self.balance}')
        else:
            print(f'Total amount: {self.income}')


print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)
