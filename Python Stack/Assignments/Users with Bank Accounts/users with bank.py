class UsersBankAccount:
    def __init__(self, int_rate , balance = 0):

        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):

        self.balance+= amount
        return self
    
    def withdraw(self , amount):
        
        if self.balance>= amount:
            self.balance-= amount
            print(f"withdraw: ${amount}")

        else:

            print("insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):

        print(f"BankAccount-Interest Rate: {self.int_rate}, Balance:${self.balance}")
        return self
    
    def yield_interest(self):

        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest

            print(f"Interest added: ${interest: .2f}")
        return self


class User:

    def __init__(self, name, int_rate = 0.01 , starting_balance = 0):

        self.name = name
        self.account = UsersBankAccount(int_rate , starting_balance)

    def display_All_Info(self):

        print(f"User: {self.name}")
        print(f"Account Balance: ${self.account.balance}")

        print(f"Ineterst Rate: {self.account.int_rate:f}%")

Ezzedin = User("Ezzedin" , int_rate = 0.02, starting_balance = 150)

Ezzedin.account.deposit(50).deposit(100).withdraw(150).yield_interest().display_account_info()

Hassoun = User("Hassoun" , int_rate = 0.02 , starting_balance = 200)
Hassoun.account.deposit(150).deposit(200).deposit(250).withdraw(300).yield_interest().display_account_info()
