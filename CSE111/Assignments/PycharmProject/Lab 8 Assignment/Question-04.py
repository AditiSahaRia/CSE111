#Task-04
#Author Aditi Saha Ria
#ID : 20101238

class Account:

    def __init__(self,balance):
        self._balance = balance

    def getBalance(self):
        return self._balance
class CheckingAccount(Account):
    numberOfAccount = '0'
    def __init__(self, x=0.0):
        self.x = x
        CheckingAccount.numberOfAccount = int(CheckingAccount.numberOfAccount)+1
        super().__init__(self.x)
        CheckingAccount.numberOfAccount = str(CheckingAccount.numberOfAccount)

    def __str__(self):
        return f'Account Balance: {self.x}'


print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)