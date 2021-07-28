class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount,):
        if BankAccount.enoughMoney(self.balance,amount):
            self.balance -= amount
            print('Balance-', self.balance)
        else:
            print("Insufficient Funds")
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    @staticmethod
    def enoughMoney(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    # def display_account_info(self, name, balance):
    #     self.name = name
    #     self.balance = balance
    #     return self

class User:
    def __init__(self, name, user_balance):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)


Bob = User("Bob", 0)
Nick = User("Nick", 1000)
Jorge = User("Jorge", 1200)


print(Bob.account.balance)
Bob.account.deposit(1000)
print(Bob.account.balance)