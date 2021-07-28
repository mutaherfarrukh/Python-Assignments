class User:		# here's what we have so far
    def __init__(self, name, user_balance):
        self.name = name
        self.user_balance = user_balance
        
    def display_balance(self):
        # self.user_balance = user_balance
        
        print(f"User: {self.name} Balance: {self.user_balance}")


    # adding the deposit method
    def make_deposit(self, amount):	
        self.user_balance += amount	


    def make_withdrawal(self, amount):
        self.user_balance -= amount


Bob = User("Bob", 600)
Nick = User("Nick", 1000)
Jorge = User("Jorge", 1200)



Bob.make_deposit(200)
Bob.make_deposit(100)
Bob.make_deposit(50)
Bob.make_withdrawal(800)
Bob.display_balance()

Nick.make_deposit(150)
Nick.make_deposit(550)
Nick.make_withdrawal(800)
Nick.make_withdrawal(50)
Nick.display_balance()

Jorge.make_deposit(200)
Jorge.make_withdrawal(100)
Jorge.make_withdrawal(250)
Jorge.make_withdrawal(50)
Jorge.display_balance()