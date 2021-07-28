class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance): 
    # your code here! (remember, instance attributes go here)
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        print(self.name, 'Balance+', self.balance)
        return self
    def withdraw(self, amount,):
        if BankAccount.enoughMoney(self.balance,amount):
            self.balance -= amount
            print(self.name, 'Balance-', self.balance)
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
    def display_account_info(self, name, balance):
        self.name = name
        self.balance = balance
        return self
    def yield_interest(self, int_rate):
        if self.balance>0:
            self.balance = self.balance + self.balance*int_rate
        return self

# class user.account(BankAccount):
#     def __init__(self, name, int_rate, balance):
#         super().__init__(name, int_rate, balance)

Alex = BankAccount("Alex", 0.01, 500)
Bob = BankAccount("Bob", 0.05, 1500)

# Alex.deposit(200)
# Alex.deposit(100)
# Alex.deposit(300)
Alex.deposit(100).deposit(300)
print(Alex.balance)
Alex.withdraw(400)
print(Alex.balance)
Alex.yield_interest(0.05)
print(Alex.balance)

# Bob.deposit(500)
# Bob.withdraw(800)
Bob.deposit(100).deposit(300)
print(Alex.balance)
print(Bob.balance)
Bob.yield_interest(0.03)
print(Bob.balance)

