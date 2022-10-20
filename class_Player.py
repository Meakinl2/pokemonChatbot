import os
import pickle 
from ProjectDataCleaning.fileControl import *
from class_Pokemon import Pokemon
import user_inputs

class Player:
    def __init__(self):
        self.money = 0
        self.inventory = {}
        self.party = []

        user_inputs.pickPlayerName(self)
        starterID, nickname = user_inputs.pickStartingPokemon(self)
        self.party.append(Pokemon(starterID,5,5,"Player"))
        self.party[0].nickname = nickname

    def reorderParty():
        pass


    def moveToParty(self):
        pass


    def moveToStorage(self):
        pass
        
    
    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Money: {self.money}")
        print(f"Current Party: ")
        for pokemon in self.party:
            print(f" -{pokemon.nickname} the Lvl {pokemon.level} {pokemon.species} ")


    def savePlayerData(self):
        pass

    # Test Functions


    # End of Player class


player = Player()
player.printStats()
