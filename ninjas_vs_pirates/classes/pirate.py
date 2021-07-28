class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.bac = 1

    def show_stats( self ):
        if Pirate.check_stats(self.health):
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nBAC: {self.bac}\n")

    def spar( self , ninja ):
        print("Pirate attacks with a sword!!")
        ninja.health -= self.strength * self.bac
        print("Pirates takes a swig of alcohol")
        self.bac += 1
        return self

    def drenken_rage(self):
        print("Rum Rage!!")
        self.health = 1000
        self.bac = 1
        self.strength = 25
        self.speed = 25
        return self

    @staticmethod
    def check_stats(health):
        if health < 0:
            print("K.O. pirate no longer able to fight")
            return False
        else:
            return True