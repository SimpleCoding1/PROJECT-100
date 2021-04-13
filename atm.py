import random
class atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        self.balance=random.randint(10000,100000)
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("LOW BALANCE")
        else:
            self.balance-=amount
            print("withdrawing",amount,"from",self.cardnumber)

    def add_money(self,amount):
        self.balance+=amount
        print("new balance is",self.balance)


a=atm(4340,45676)
a.withdraw(4000)
a.add_money(5000)