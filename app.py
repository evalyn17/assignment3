import Account,savingAccount, chequingAccount
class program:
    def __init__(self):
        self.AccountMenu = ()
        self.MainMenu = ()
    
    def MainMenu(self, account):
        account = account()
        choice = 0
        while choice != 2:
            print("1 for Account") 
            print("2 for Exit")
        if choice == 1:
            accountNo = int(input("Enter Account Number: "))
            account = self.bank.search_account(accountNo)
            if account:
                self.AccountMenu(account)
        else:
            print("Exiting Menu!")
    
    def AccountMenu(self, account):
        account = Account()
        choice = 0
        while choice != 2:
            print("1 for Deposit")
            print("2 for Withdraw")
            choice = input("Enter Action: ")
        if choice == 1:
            amount = int(input("Enter Amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter Amount: "))
            account.withdraw(amount)
        else:
            print("Exiting Menu!")
    