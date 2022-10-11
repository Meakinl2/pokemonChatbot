import os
import pickle
from ProjectDataCleaning.fileControl import *

class pokemon:
    def __init__(self, speciesID):
        # Load in Data from the data file
        pokemonInfoFile = selectFile(["DataTables"],"pokemonBaseStats.txt")
        pokemonInfo = readFile(pokemonInfoFile)
        speciesInfo = pokemonInfo[speciesID]
        
        # Set Species and inital Nickname of pokemon
        self.species = speciesInfo[1]
        self.nickname = speciesInfo[1]

        # Setup starting stats for pokemon, will only run on initial creation
        # Will add some slight variation 
        self.types = [speciesInfo[2],speciesInfo[3]]
        self.baseHP = speciesInfo[5]
        self.baseATK = speciesInfo[6]
        self.baseDEF = speciesInfo[7]
        self.baseSPA = speciesInfo[8]
        self.baseSPD = speciesInfo[9]
        self.baseSPE = speciesInfo[10]
        if speciesInfo[11] == "true":
            self.isLegendary = True
        else:
            self.isLegendary = False
    
    # Pemanent Stat changes (eg. from level up)
    def levelUp(self):
        pass


    # Temporary Stat changes (eg. from battle buffs/debuffs)
    def currentStats(self):
        pass
    

    def changeCurrentStats(self):
        pass
    

    def changeNickname(self, newNickname):
        self.nickname = newNickname


myPokemon = pokemon(1)
print(f"{myPokemon.species} has HP:{myPokemon.baseHP}, ATK:{myPokemon.baseATK}, DEF:{myPokemon.baseDEF}, SPA:{myPokemon.baseSPA}, SPD:{myPokemon.baseSPD}, SPE{myPokemon.baseSPE}")