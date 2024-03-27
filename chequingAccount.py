import Account

class checqueingAccount(Account):
    def __init__(self):
        self.min_balance = 800
    
    def withdraw(self, amount):
        if amount <= self.min_balance:
            self.min_balance -= amount
            print("Current Balance: ", self.min_balance)
        else:
            print("You Do Not Have Enough Funds!")
    
    def deposit(self, amount):
        if amount > 0:
            self.min_balance += amount
            print("Current Balance: ", self.min_balance)
        else:
            print("Invalid Amount!")