class User:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} deposit {amount}")
        self.display_user_balance()
        return self

    def make_withdrawal(self, amount):
        if self.account_balance <= 0:
            print("Insufficient balance")
        else:
            self.account_balance -= amount <= 0
            print(f"{self.name} withdraw {amount}")
            self.display_user_balance()
            return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} Dollar")
        return self

    def transfer_money(self, other_user, amount):
        if self.account_balance - amount < 0:
            print("their is no money")
        else:
            self.account_balance -= amount
            other_user.account_balance += amount
            print(f"{self.name} transfer {amount} to {other_user.name}")
            self.display_user_balance()
            return self


yousef = User("yousef", "brighith.y@live.com")
ali = User("ali", "ali.y@live.com")
mohamed = User("mohamed", "mohamed.y@live.com")


yousef.make_deposit(100).make_deposit(
    360).make_withdrawal(30).make_deposit(140)
yousef.display_user_balance()
ali.make_deposit(1209).make_deposit(
    3900).make_withdrawal(900).make_withdrawal(300)
ali.display_user_balance()
mohamed.make_deposit(5900)
mohamed.make_withdrawal(320)
mohamed.make_withdrawal(400)
mohamed.make_withdrawal(2000)
mohamed.display_user_balance()
yousef.transfer_money(ali, 20000)
yousef.display_user_balance()
ali.display_user_balance()
