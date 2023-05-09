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
        else:
            print("your account balance is negative")
        return self


class User:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self.account

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self.account

    def display_user_balance(self):
        print(f" user:{self.name} has {self.account} Dollar")
        return self.account

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self.account

    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)


acount1 = BankAccount(int_rate=5, balance=600)
acount2 = BankAccount(int_rate=4.5, balance=8000)
acount1.deposit(500).deposit(637).deposit(800).withdraw(
    400).yield_interest().display_account_info()
acount2.deposit(700).deposit(9000).withdraw(400).withdraw(300).withdraw(
    100).withdraw(50).yield_interest().display_account_info()
