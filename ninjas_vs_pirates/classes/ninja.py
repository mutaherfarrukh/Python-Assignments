class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.chakra = 100
        
    def show_stats( self ):
        if Ninja.check_stats(self.health):
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nChakra: {self.chakra}\n")
        

    def shuriken( self , enemy ):
        print("Ninja attacks with a slash")
        enemy.health -= (self.speed * self.strength/2)
        pirate.health -= 15
        self.chakra -= 10
        return self

    def sage_mode(self):
        print("Toad Sage!!")
        self.health = 100
        self.chakra = 100
        self.strength = 25
        self.speed = 25
        return self

    @staticmethod
    def check_stats(health):
        if health < 0:
            print("K.O. ninja  no longer able to fight")
            return False
        else:
            return True