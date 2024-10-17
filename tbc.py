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
        print(f"{name}")
        print(f"{hitPoints}")
        print(f"{hitChance}")
        print(f"{maxDamage}")
        print(f"{armor}")
        
def main():
    hero = Character()
    hero.name = "Damian"
    hero.printStats()
        
main()