from bank import Account, bank, savingAccount, chequeingAccount

class Program:
    def __init__(self):
        self.bank = bank()
        self.current_account = None
    
    def showMainMenu(self):
        while True:
            print("~Banking Main Menu~")
            print("1. Select Account")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.selectAccount()
            elif choice == '2':
                print("Exiting Menu...")
                break
            else:
                print("Invalid!")

    def selectAccount(self):
        accountNo = int(input("Enter Account Number: "))
        account = self.bank.search_account(accountNo)
        if account:
            self.current_account = account
            self.showAccountMenu()
        else:
            print("Account Not Found!")

    def showAccountMenu(self):
        while True:
            print("~Account Menu~")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.checkBalance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Exiting Menu...")
                break
            else:
                print("Invalid!")

    def checkBalance(self):
        if self.current_account:
            print("Account Number: ", self.current_account.accountNo)
            print("Account Name: ", self.current_account.account_name)
            print("Chequing Balance: ", self.current_account.chequeingAccount.balance)
            print("Savings Balance: ", self.current_account.savingAccount.balance)
        else:
            print("No Account was Selected!")

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        if self.current_account:
            self.current_account.deposit(amount)
        else:
            print("No Account was Selected!")

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        if self.current_account:
            self.current_account.withdraw(amount)
        else:
            print("No Account was Selected!")

if __name__ == "__main__":
    program = Program()
    program.showMainMenu()