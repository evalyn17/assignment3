from bank import Bank
from Account import Account
from checqueingAccount import checqueingAccount
from savingAccount import savingAccount

def showMainMenu(bank):
    while True:
        print("\nMain Menu")
        print("1. Select Account")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            accountNo = int(input("Enter Account Number: "))
            account = bank.search_account(accountNo)
            if account:
                showAccountMenu(account)
            else:
                print("Account not found.")
        elif choice == 2:
            break
        else:
            print("Invalid! Please enter again!")


def showAccountMenu(account):
    while True:
        print("\nAccount Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Account Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account.profile()
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            break
        else:
            print("Invalid! Please enter again!")

# Main program
bank = Bank()
bank.create_accounts()
showMainMenu(bank)

