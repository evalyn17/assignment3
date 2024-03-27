import Account
import chequingAccount
import savingAccount

first_account = ((Account, 1001, "Bob"), (Account, 1002, "Alex"), (Account, 1003, "May"), (Account, 1004, "Tommy"), (Account, 1005, "Eva"))
acc_number = int(input("Enter The Account Number"))
for i in range(0, len(first_account)):
    if first_account[i].accountNo == acc_number:
        print("Account Exist")
        first_account[i].profile()
        amount = int(input("Enter the amount you want to withdraw"))
        first_account[i].withdraw(amount)