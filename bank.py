import Account

class bank:
    bank_name = "TD"

    def __init__(self,accountNo):
        self.accountNo = accountNo

        
lst_accounts = ((Account, 1001, "Bob"), (Account, 1002, "Alex"), (Account, 1003,"May"), (Account, 1004,"Tommy"), (Account, 1005,"Eva"))
accountNo = int(input("Enter The Account Number: "))
for i in range(0,len(lst_accounts)):
    if lst_accounts[i].accountNo:
        print("Acccount Exists")
        lst_accounts[i].profile()
        amount = int(input("Enter the amount to withdraw"))
        lst_accounts[i].withdraw(amount)