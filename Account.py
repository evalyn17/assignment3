class Account:
    #Attributes for the Account class 
    def __init__(self, accountNo, account_name, savingAccount, chequeingAccount):
        self.accountNo = accountNo
        self.account_name = account_name
        self.savingAccount = savingAccount()
        self.chequeingAccount = chequeingAccount()
    
    #stating the user's account info and balance
    def profile(self):
        print("Account Number: ", self.accountNo)
        print("Account Name: ", self.account_name)
        print("Chequing Balance: ", self.chequeingAccount.balance)
        print("Savings Balance: ", self.savingAccount.balance)
    
    def withdraw(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequing"))
        if choice == 1:
            self.savingAccount. withdraw(amount)
        else:
            self.chequingAccount.withdraw(amount) 

    def deposit(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequeing"))
        if choice == 1:
            self.savingAccount.deposit(amount)
        else:
            self.chequeingAccount.deposit(amount)

class chequeingAccount(Account):
    def __init__(self):
        self.balance = 500
        self.overdraft_limit = 1000
    
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Current Balance: ", self.balance)
        else:
            print("You Do Not Have Enough Funds!")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Current Balance: ", self.balance)
        else:
            print("Invalid Amount!")

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