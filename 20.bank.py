class account:
    def __init__(self,nm,accnum,acctype,bal):
        self.name=nm
        self.accountnumber=accnum
        self.type=acctype
        self.balance=bal

    def deposit(self):
        amt=int(input("Enter the amount to be deposited ="))
        self.balance+=amt
        print("New balance =",self.balance)

    def withdraw(self):
        if(self.balance<500):
            print("Insufficient balance !")
        else:
            amt=int(input("Enter an amount to withdraw ="))
            self.balance-=amt
            print("New balance =",self.balance)

    def display(self):
        print("ACCOUNT DETAILS")
        print("Name of account holder =",self.name)
        print("Account number =",self.accountnumber)
        print("Type of account =",self.type)
        print("Available balance =",self.balance)

s=account(input("Enter account name ="),int(input("Enter account number =")),input("Enter account type[current/savings] ="),int(input("Enter available balance =")))
print("----------BANKING---------")
print("\n1.ACCOUNT DETAILS\n2.DEPOSIT\n3.WITHDRAW\n0.EXIT")
def bank():
    n = int(input("\nenter choice:"))
    if (n == 1):
        s.display()
        return bank()
    elif n == 2:
        s.deposit()
        return bank()
    elif n == 3:
        s.withdraw()
        return bank()
    elif n == 0:
        print("THANK YOU")
        return 0
    else:
        print("INVALID ENTRY!")
        print("please enter valid choice\n")
        return bank()
bank()
