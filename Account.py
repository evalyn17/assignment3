class Account:
    bank_name = "TD"
    def __init__(self, accountNo, account_name, savingAccount, chequingAccount):
        self.accountNo = accountNo
        self.account_name = account_name
        self.savingAccount = savingAccount()
        self.chequingAccount = chequingAccount()
      
    def profile(self):
        print(self.accountNo, self.account_name)
        print("Current Balance: ", self.chequingAccount.balance)
    
    def withdraw(self, amount):
        choice = input("Saving or Chequing")
        if choice == 1:
            self.savingAccount. withdraw(amount)
        else:
            self.chequingAccount.withdraw(amount) 

    def deposit(self, amount):
        choice = input("Saving or Chequing")
        if choice == 1:
            self.savingAccount.deposit(amount)
        else:
            self.chequingAccount.deposit(amount)
    
 
