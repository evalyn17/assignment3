from Account import Account, savingAccount, chequeingAccount

class bank:
    bank_name = "TD"

#Attributes for the bank class
    def __init__(self):
        self.list_account = []
        self.search_accounts = ()
    
#Creating and listing the 5 different bank accounts 
    def create_accounts(self):
        self.list_account.append(Account, 1001, "Bob", savingAccount)
        self.list_account.append(Account, 1002, "Alex", chequeingAccount)
        self.list_account.append(Account, 1003,"May", savingAccount)
        self.list_account.append(Account, 1004,"Tommy",chequeingAccount)
        self.list_account.append(Account, 1005,"Eva",savingAccount)
   
    def search_account(self, accountNo):
        for account in self.list_account:
            if account.accountNo == accountNo:
                return account 

#Asking user for bank info for withdrawal/deposit
accountNo = int(input("Enter Account Number: "))
account_name = input("Enter Name: ")
choice = int(input("Enter 1 for Savings or 2 for Chequeing: "))

if choice == 1:
   saving_account =savingAccount()
   chequeing_account = chequeingAccount()
else:
    saving_account = savingAccount()
    chequeing_account = chequeingAccount()

account = Account(accountNo, account_name, savingAccount, chequeingAccount )
account.profile() 

#Asking user for withdrawal/deposit money and doing transaction
transaction = int(input(" Enter 1 for Deposit ot 2 for Withdrawal: "))
amount = int(input("Enter The Amount: "))

if transaction == 1:
    account.deposit(amount)
elif transaction == 2:
    account.withdraw(amount)
else:
    print("Transaction Did Not Go Through!")