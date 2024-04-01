class Account:
    def __init__(self, accountNo, account_name, savingAccount, checqueingAccount):
        self.accountNo = accountNo
        self.account_name = account_name
        self.savingAccount = savingAccount
        self.checqueingAccount = checqueingAccount
    
    def profile(self):
        print("Account Number:", self.accountNo)
        print("Account Name:", self.account_name)
        print("Chequing Balance:", self.checqueingAccount.balance)
        print("Savings Balance:", self.savingAccount.balance)
    
    def withdraw(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequing: "))
        if choice == 1:
            self.savingAccount.withdraw(amount)
        elif choice == 2:
            self.checqueingAccount.withdraw(amount)
        else:
            print("Invalid choice!")

    def deposit(self, amount):
        choice = int(input("Choose 1 for Saving or 2 for Chequing: "))
        if choice == 1:
            self.savingAccount.deposit(amount)
        elif choice == 2:
            self.checqueingAccount.deposit(amount)
        else:
            print("Invalid choice!")

