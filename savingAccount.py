import Account
class savingAccount(Account):
    def __init__(self):
        self.balance = 1000
        self.min_balance = 200
    
    def withdraw(self, amount):
        if amount - self.balance >= self.min_balance:
            self.balance -= amount 
            print("Current Balance: ", self.balance)
        else:
            print("You Do Not Have Enough Funds!")
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Current Balance: ", self.balance)
        else:
            print("Invalid Amount!")