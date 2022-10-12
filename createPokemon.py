import os, csv, pickle, math, random
from struct import calcsize
from ProjectDataCleaning.fileControl import *

# Pokemon Levelling is quite complicated apparently, I kind of knew that before, but still....
# Convoluted seems now a better word, levelling is quite simple

# Stats are based on this formula and I think it is redone every levelup, based on experience
# Level: 1-100; IV: 0 - 31 per Stat; EV: 0 - 255 per stat, 510 across all stats cumulatively (Wild Pokemon have none)
# Nature Modifier for health should always be just one and will be either 0.9,1 or 1.1 for all other stats
def calculateStat(base,level,IV,EV,isHP,natureModifier):
    stat = ((2 * base + IV + (EV//4)) * level) // 100
    if isHP:
        stat += (level + 5)
    stat += 5
    stat *= natureModifier
    return stat


# I'm not actually sure if this is how IVs are generated,but it makes sense this way
def generateIVS():
    IVS = []
    for each in range(6):
        IV = random.randint(0,31)
        IVS.append(IV)
    return IVS


# Defines the basic design for each pokemon, unsure quite how much this will control at this point
# Is inital passed the SpeciesID number(from Pokedex) and the range the pokemon should be in
class pokemon:
    def __init__(self,speciesID,minLvl,maxLvl):
        # Load in Data from the data file
        pokemonInfoFile = selectFile(["DataTables"],"pokemonBaseStats.txt")
        pokemonInfo = readFile(pokemonInfoFile)
        speciesInfo = pokemonInfo[speciesID]
        
        # Set Species and inital Nickname of pokemon
        self.species = speciesInfo[1]
        self.nickname = speciesInfo[1]
        self.level = random.randint(minLvl,maxLvl)
        self.experience = 0

        # Copying Base stats out of the speciesInfo
        # Thats's: HP, ATK, DEF, SP.A, SP.D, SPE
        self.baseStats = [speciesInfo[5],speciesInfo[6],speciesInfo[7],speciesInfo[8],speciesInfo[9],speciesInfo[10]]
        self.IVs = generateIVS()
        self.EVs = [0,0,0,0,0,0]
        self.natureModifier = [1,1,1,1,1,1]
        self.types = [speciesInfo[2],speciesInfo[3]]
        if speciesInfo[11] == "true":
            self.isLegendary = True
        else:
            self.isLegendary = False

        # Calculate stats adjusted for Lvl, IVs, EVs and nature
        self.adjustedStats = []
        isHP = True
        statID = 0
        for each in self.baseStats:
            lvlAdjustedStat = calculateStat(int(self.baseStats[statID]),self.level,self.IVs[statID],self.EVs[statID],isHP,self.natureModifier[statID])
            self.adjustedStats.append(lvlAdjustedStat)
            statID += 1
            isHP = False
    


    def shouldLevelUp(self):
        # Runs whenever experience gained
        pass


    # Temporary Stat changes (eg. from battle buffs/debuffs)
    def currentStats(self):
        pass
    

    def changeCurrentStats(self):
        pass
    

    def changeNickname(self, newNickname):
        self.nickname = newNickname


for i in range(0,20):
    myPokemon = pokemon(random.randint(1,721),1,100)
    print(f"Generated Pokemon {i  +  1}")
    print(f"Species: {myPokemon.species}")
    print(f"Lvl: {myPokemon.level}")
    print(f"Base Stats: HP:{myPokemon.baseStats[0]}  ATK:{myPokemon.baseStats[1]} DEF:{myPokemon.baseStats[2]} SPA:{myPokemon.baseStats[3]} SPD:{myPokemon.baseStats[4]} SPE:{myPokemon.baseStats[5]}")
    print(f"IVs: HP:{myPokemon.IVs[0]} ATK:{myPokemon.IVs[1]} DEF:{myPokemon.IVs[2]} SPA:{myPokemon.IVs[3]} SPD:{myPokemon.IVs[4]} SPE:{myPokemon.IVs[5]}")
    print(f"EVs: HP:{myPokemon.EVs[0]} ATK:{myPokemon.EVs[1]} DEF:{myPokemon.EVs[2]} SPA:{myPokemon.EVs[3]} SPD:{myPokemon.EVs[4]} SPE:{myPokemon.EVs[5]}")
    print(f"Adjusted Stats: HP:{myPokemon.adjustedStats[0]} ATK:{myPokemon.adjustedStats[1]} DEF:{myPokemon.adjustedStats[2]} SPA:{myPokemon.adjustedStats[3]} SPD:{myPokemon.adjustedStats[4]} SPE:{myPokemon.adjustedStats[5]}")
    print("------------------------------------------------------------------")