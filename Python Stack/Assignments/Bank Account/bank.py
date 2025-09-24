class BankAccount:
    def __init__(self, int_rate , balance = 0):

        self.int_rate = int_rate

        self.balance = balance

    def deposite(self,amount):

        self.balance+= amount
        return self
    
    def withdraw(self,amount):

        if self.balance>= amount:
            self.balance-= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    
    def display_account_info(self):
        print(f"BankAccount-Interest Rate: {self.int_rate}, Balance:${self.balance}")
        return self
    
    def yield_interst(self):
        if self.balance>0:
            interest=self.balance*self.int_rate
            self.balance+=interest
        return self
    
Ezzedin =BankAccount(0.02,100)
Hassoun =BankAccount(0.02,200)

# the first account, make 3 deposits and 1 withdrawal
Ezzedin.deposite(50).deposite(100).deposite(200).withdraw(40).yield_interst().display_account_info()
# the second account, make 2 deposits and 4 withdrawals
Hassoun.deposite(50).deposite(70).withdraw(50).withdraw(100).withdraw(30).withdraw(40).yield_interst().display_account_info()