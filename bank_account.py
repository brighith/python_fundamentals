class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Insufficient balance")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate/100)
        return self


acount1 = BankAccount(int_rate=5, balance=600)
acount2 = BankAccount(int_rate=4.5, balance=8000)
acount1.deposit(500).deposit(637).deposit(800).withdraw(
    400).yield_interest().display_account_info()
acount2.deposit(700).deposit(9000).withdraw(400).withdraw(300).withdraw(
    100).withdraw(50).yield_interest().display_account_info()
