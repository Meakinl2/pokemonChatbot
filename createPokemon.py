import os
import pickle

class pokemon:
    def __init__(self, species):
        self.species = species
    
    # Setup starting stats for pokemon, will only run on initial creation
    def startingStats(self, species):
        self.baseHP = 1
        self.baseATK = 1
        self.baseDEF = 1
        self.baseSPE = 1
        self.baseSPA = 1
        self.baseSPD = 1
        #Access file and use species to find all base stats and then add some sight variation
        pass
    
    def changeBaseStats(self):
        pass

    def currentStats(self):
        pass
    
    def changeCurrentStats(self):
        pass
    
    def changeNickname(self, newNickname):
        self.nickname = newNickname


poke1 = pokemon("Pickachu", "Pika")
print(poke1.nickname)
poke1.changeNickname("Piko")
print(poke1.nickname)