import random

class Character(object):
    def __init__(self, name = "Damian",
                 hitPoints = 15,
                 hitChance = 45,
                 maxDamage = 6,
                 armor = 1):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor



    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = value
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
    
    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value

    def printStats(self):
        print(f"""
        Name : {self.name}
        Health : {self.hitPoints}
        Hit Chance : {self.hitChance}
        Max Damage : {self.maxDamage}
        Armor : {self.armor}
        """)
        
    def hit(self, enemy):
        if random.randint(1, 100) < self.hitChance:
            print (f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print (f" for {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name}'s armor absorbed {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses {enemy.name}")
            
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
        
    def basicFight(player1, player2):
        keepGoing = True
        while keepGoing:
            player1.hit(player2)
            player2.hit(player1)
            
            print(f"{player1.name} HP : {player1.hitPoints}")
            print(f"{player2.name} HP : {player2.hitPoints}")
            print()
            
            if player1.hitPoints <= 0:
                print(f"{player1.name} loses")
                keepGoing = False
            elif player2.hitPoints <= 0:
                print(f"{player2.name} loses")
                keepGoing = False
                
            dummy = input("Press <ENTER> for another round")
        
def main():
    hero = Character()
    hero.name = "Damian"
    hero.printStats()
    
        
if __name__ == "__main__":
    main()