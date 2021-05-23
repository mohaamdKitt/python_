

class User(BankAccount):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account_balance=BankAccount(int_rate=0.02, balance=0)
    
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.deposit(amount)
class BankAccount:
    def __init__ (self,int_rate,balance):
        self.int_rate=0.01
        self.balance=0

    def deposit (self,amount):
        self.balance += amount
        return self

    def withdraw (self,amount):
        fee=5
        if self.balance >= amount:
            self.balance -= amount
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - amount - fee
            
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest (self):
        if self.balance>0 :
            self.balance += self.balance * self.int_rate
        return self    

account_1=BankAccount (.01 , 0)
account_2=BankAccount (.02 , 0)

account_1.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
account_2.deposit(1000).deposit(300).withdraw(2000).withdraw(1000).yield_interest().display_account_info()



mahmood=User("mahmood","dcmlkdmckl@gamil.com")
mostafa=User("mostafa", "dcnldksn@gmail.com")
mohamad=User("mohamad", "dlkjnclndlkcn@gmail.com")

mahmood.deposit(10000)
mahmood.deposit(2000)


mahmood.transfer_money(mohamad, 10000)
mahmood.display_user_balance()
mohamad.display_user_balance()

