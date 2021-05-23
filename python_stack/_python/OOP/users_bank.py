class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account=Bankaccount()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        
        
        return self

    def make_withdrawal(self, amount):
        if  self.account.balance >= amount:
             self.account.withdrawal(amount)
    
    def account_info(self):
        print(f"name: {self.name} account balance{self.account.balance}")
    
    def transfare_money(self, other_users, amount):
        if amount <= self.account.balance:
            self.account.balance -= amount
            other_users.account.balance += amount
    

class Bankaccount:
    def __init__(self, intrate=0.02, balance=0):
        self.intrate=intrate
        self.balance=balance
        
    
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdrawal(self, amount):
        
            self.balance-=amount
   

    def yield_interest(self):#haram
        self.balance=self.balance + (self.balance*self.intrate)



mohammad = User("Adel", "jdbvkjdbkvs")
mahmmod=User("mahmmod","vfuuigvvd")
mohammad.make_deposit(5000).make_withdrawal(4000)
mohammad.transfare_money(mahmmod, 500)
mohammad.account_info()
mahmmod.account_info()







