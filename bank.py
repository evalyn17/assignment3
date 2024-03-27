from Account import Account, checqueingAccount, savingAccount

class bank:
    bank_name = "TD"

    def __init__(self):
        self.list_account = []
        self.search_accounts = ()
    
#Listiing the 5 different bank accounts 
    def create_accounts(self):
        self.list_account.append(Account, 1001, "Bob")
        self.list_account.append(Account, 1002, "Alex")
        self.list_account.append(Account, 1003,"May")
        self.list_account.append(Account, 1004,"Tommy")
        self.list_account.append(Account, 1005,"Eva")
   
    def search_account(self, accountNo):
        for account in self.list_account:
            if account.accountNo == accountNo:
                return account 

#Asking usert for input/bank info
accountNo = int(input("Enter Account Number: "))
bank = bank()
account = bank.search_account(accountNo)
if account:
    account.profile()
else:
    print("Sorry! Account Not Found!")