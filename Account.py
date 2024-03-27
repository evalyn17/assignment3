class Account:
    #Attributes for the Account class 
    def __init__(self, accountNo, account_name, savingAccount, chequingAccount):
        self.accountNo = accountNo
        self.account_name = account_name
        self.savingAccount = savingAccount()
        self.chequingAccount = chequingAccount()
    
    #stating the user's account info and balance
    def profile(self):
        print("Account Number: ", self.accountNo)
        print("Account Name: ", self.account_name)
        print("Chequing Balance: ", self.chequingAccount.balance)
        print("Savings Balance: ", self.savingAccount.balance)
    
    def withdraw(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequing"))
        if choice == 1:
            self.savingAccount. withdraw(amount)
        else:
            self.chequingAccount.withdraw(amount) 

    def deposit(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequing"))
        if choice == 1:
            self.savingAccount.deposit(amount)
        else:
            self.chequingAccount.deposit(amount)

accountNo = int(input("Enter Account Number: "))
account_name = input("Enter Name: ")
