import Account

class bank:
    bank_name = "TD"

    def __init__(self):
        self.list_account = []
        self.search_account = ()
    
    def list_account(self):
        self.list_account.append(Account, 1001, "Bob")
        self.list_account.append(Account, 1002, "Alex")
        self.list_account.append(Account, 1003,"May")
        self.list_account.append(Account, 1004,"Tommy")
        self.list_account.append(Account, 1005,"Eva")
   
    def search_account(self, accountNo):
        for account in self.list_account:
            if account.accountNo == accountNo:
                return account