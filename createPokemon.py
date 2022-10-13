import os, csv, pickle, math
from random import randint
from dictonaries import *
from ProjectDataCleaning.fileControl import *

# Pokemon Levelling is quite complicated apparently, I kind of knew that before, but still....
# Convoluted seems now a better word, leveling is quite simple

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
# That is to say I know they ar eat least partial random, but I'm unsure if they are in some way centrally weighted
def generateIVS():
    IVS = []
    for each in range(6):
        IV = randint(0,31)
        IVS.append(IV)
    return IVS


# Defines the basic design for each pokemon, unsure quite how much this will control at this point
# Is inital passed the SpeciesID number(from Pokedex) and the range the pokemon should be in
# Context determines whether or not specific things should happen (such as giving trainer pokemon EVs)
class pokemon:
    def __init__(self,speciesID,minLvl,maxLvl,context):
        # Get the basic stats, set required things as they are required to be
        self.copyBaseValues(speciesID)
        self.nickname = self.species
        self.allowedEvolve = True
        
        # Generate all semi-random attributes
        self.level = randint(minLvl,maxLvl)
        self.experience = levelingBounds[self.level]
        self.IVs = generateIVS()
        self.EVs = [0,0,0,0,0,0]
        self.natureModifier = [1,1,1,1,1,1]
        
        # Apply all context specfic attribute alterations
        if context == "Trainer":
            self.setTrainerEVs()

        # Sets "adjusted" stats and give the pokemon its starting moveset
        self.calculateAdjustedStats()
        # self.actualStats = self.adjustedStats()
        self.determineStartMoveset()
    
    # Copying all relevant information from baseStats table
    # Used initaily and upon evolution to update relevant attributes
    def copyBaseValues(self, speciesID):
        pokemonInfoFile = selectFile(["DataTables"],"pokemonBaseStats.txt")
        pokemonInfo = readFile(pokemonInfoFile)
        speciesInfo = pokemonInfo[speciesID]
        
        self.species = speciesInfo[1]

        try: 
            self.evolveTo = int(speciesInfo[13])
            self.evolveAtLevel = int(speciesInfo[14])
        except:
            self.evolveTo = ""
            self.evolveAtLevel = 1000

        self.baseStats = [int(speciesInfo[5]),int(speciesInfo[6]),int(speciesInfo[7]),int(speciesInfo[8]),int(speciesInfo[9]),int(speciesInfo[10])]
        self.types = [speciesInfo[2],speciesInfo[3]]
        
        if speciesInfo[11] == "true":
            self.isLegendary = True
        else:
            self.isLegendary = False

    # Just increase the pokemons experience by a given amount and runs levelUp check
    def addExperience(self,newExperience):
        self.experience += newExperience
        self.levelUp()
        

    # Calculate stats adjusted for Lvl, IVs, EVs and nature
    def calculateAdjustedStats(self):
        self.adjustedStats = []
        isHP = True
        statID = 0
        for each in self.baseStats:
            lvlAdjustedStat = calculateStat(int(self.baseStats[statID]),self.level,self.IVs[statID],self.EVs[statID],isHP,self.natureModifier[statID])
            self.adjustedStats.append(lvlAdjustedStat)
            statID += 1
            isHP = False


    # Runs whenever experience gained , to detetmine if levelUp should occur
    def levelUp(self):
        fullyLeveled = False
        while not fullyLeveled and self.level < 100:
            nextLevel = self.level + 1
            nextBound =  levelingBounds[nextLevel]
            if self.experience <= nextBound:
                fullyLeveled = True
            else:
                self.level += 1
                self.calculateAdjustedStats()
                print(f"{self.nickname} has Leveled Up.")
                print(f"{self.nickname} is now Level {self.level}")
                print(f"HP:{self.adjustedStats[0]} ATK:{self.adjustedStats[1]} DEF:{self.adjustedStats[2]} SPA:{self.adjustedStats[3]} SPD:{self.adjustedStats[4]} SPE:{self.adjustedStats[5]}")
                self.evolve()
        

    # Following levelUp, checks if the pokemon should levelUp
    def evolve(self):
        if self.level >= self.evolveAtLevel and self.allowedEvolve:
            print(f"{self.nickname} is evolving!")
            initalSpecies = self.species
            self.copyBaseValues(self.evolveTo)
            print(f"{self.nickname} evolved in {self.species}")
            if self.nickname == initalSpecies:
                self.nickname = self.species
            self.calculateAdjustedStats()
            

    # Trainer pokemon are given EVs based on their difficulty to make them more challenging than wild pokemon
    def setTrainerEVs(self):
        pass

    
    # Determines the moves a pokemon should start with based on the allowed moves
    def determineStartMoveset(self):
        pass


    # Calculates a pokemons actual stats following modifers such as buffs/debuffs and held items
    def determineActualStats(self):
        pass
    

    def changeNickname(self, newNickname):
        self.nickname = newNickname
    
    # End of pokemon class


# Test Functions to check stuff is working correctly
# Generates random Test pokemon to check pokemon generation is working
def generateTestPokemon(amount,minLvl,maxLvl,):
    for i in range(0,20):
        myPokemon = pokemon(randint(1,721),1,100,"Wild")
        print(f"Generated Pokemon {i  +  1}")
        print(f"Species: {myPokemon.species}")
        print(f"Typing: {myPokemon.types[0]}  {myPokemon.types[1]} ")
        print(f"Lvl: {myPokemon.level} from Exp: {myPokemon.experience} ")
        print(f"Base Stats: HP:{myPokemon.baseStats[0]}  ATK:{myPokemon.baseStats[1]} DEF:{myPokemon.baseStats[2]} SPA:{myPokemon.baseStats[3]} SPD:{myPokemon.baseStats[4]} SPE:{myPokemon.baseStats[5]}")
        print(f"IVs: HP:{myPokemon.IVs[0]} ATK:{myPokemon.IVs[1]} DEF:{myPokemon.IVs[2]} SPA:{myPokemon.IVs[3]} SPD:{myPokemon.IVs[4]} SPE:{myPokemon.IVs[5]})")
        print(f"EVs: HP:{myPokemon.EVs[0]} ATK:{myPokemon.EVs[1]} DEF:{myPokemon.EVs[2]} SPA:{myPokemon.EVs[3]} SPD:{myPokemon.EVs[4]} SPE:{myPokemon.EVs[5]})")
        print(f"Adjusted Stats: HP:{myPokemon.adjustedStats[0]} ATK:{myPokemon.adjustedStats[1]} DEF:{myPokemon.adjustedStats[2]} SPA:{myPokemon.adjustedStats[3]} SPD:{myPokemon.adjustedStats[4]} SPE:{myPokemon.adjustedStats[5]}")
        print("------------------------------------------------------------------")

# Allows adding experience amounts to check the pokemon is levelin up appropriatley
def testLeveling():
    myPokemon = pokemon(randint(1,721),1,1,"Wild")
    while True:  
        experienceAdd  = int(input("Add Experience: \n> "))
        myPokemon.experience += experienceAdd
        myPokemon.levelUp()

testLeveling()