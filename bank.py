from Account import Account
from savingAccount import savingAccount 
from checqueingAccount import checqueingAccount

class Bank:
    bank_name = "TD"

    # Attributes for the bank class
    def __init__(self):
        self.list_account = []

    # Creating and listing the 5 different bank accounts 
    def create_accounts(self):
        self.list_account.append(Account(1001, "Bob", savingAccount(), checqueingAccount()))
        self.list_account.append(Account(1002, "Alex", checqueingAccount(), savingAccount()))
        self.list_account.append(Account(1003, "May", savingAccount(), checqueingAccount()))
        self.list_account.append(Account(1004, "Tommy", checqueingAccount(), savingAccount()))
        self.list_account.append(Account(1005, "Eva", savingAccount(), checqueingAccount()))
   
    def search_account(self, accountNo):
        for account in self.list_account:
            if account.accountNo == accountNo:
                return account 

