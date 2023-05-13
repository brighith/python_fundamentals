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
        print(f" user:{self.name} has {self.account.balance} Dollar")

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.make_deposit(amount)
        return self.account


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0:
            print("Insufficient funds")
            self.balance -= 5

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


yousef = User("yousef", "brighith.y@live.com")
satha = User("satha", "satah@gmail.com")

yousef.make_deposit(100)
print(yousef.display_user_balance())
yousef.make_withdrawal(20)
print(yousef.display_user_balance())
yousef.transfer_money(satha, 40)
print(yousef.display_user_balance())
print(satha.display_user_balance())
