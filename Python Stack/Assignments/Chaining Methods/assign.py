class User:
    def __init__(self,name,balance=0):

        self.name=name
        self.balance=balance

    def make_deposit(self,amount):

        self.balance+=amount
        return self
    
    def make_withdraw(self,amount):

        self.balance-=amount
        return self
    
    def display_userBalance(self):

        print(f"User:{self.name},Balance:${self.balance}")
        return self
    
    def transfer_money(self,other_user,amount):

        self.make_withdraw(amount)
        other_user.make_deposit(amount)

        print(f"{self.name} transfered ${amount} to {other_user.name}")
        return self
    
user1=User("Ezzedin")
user2=User("Mahmoud")
user3=User("Hassoun")

# From assignment (User):First user make 3 deposite and 1 withdraw using chaining method

user1.make_deposit(200).make_deposit(300).make_deposit(50).make_withdraw(55).display_userBalance()

# From assignment (User):Second user make 2 deposite and 2 withdraw using chaining method

user2.make_deposit(200).make_deposit(150).make_withdraw(100).make_withdraw(50).display_userBalance()

# From assignment (User):Third user make1 deposite and 3 withdraw using chaining method

user3.make_deposit(500).make_withdraw(200).make_withdraw(50).make_withdraw(55).display_userBalance()

# From assignment (User):Transfer money from user1 to user3
user1.transfer_money(user3,55).display_userBalance()
user3.display_userBalance()
