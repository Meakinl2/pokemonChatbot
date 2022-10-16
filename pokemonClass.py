import os, csv, pickle, math
from random import randint
from dictonaries import *
from ProjectDataCleaning.fileControl import *
from PokemonFormulae import *


# Saves having to open the move file everytime any move is used.
class move:
    def __init__(self,moveID):
        movesFile  = selectFile(["DataTables"], "moveInformation.txt")
        moveInformation = ""
        self.name = ""
        self.typing = []
        self.power = 0
        self.accuracy = 0
        self.pp = 0



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
        self.EVs = [0,0,0,0,0,0]
        self.IVS = []
        for each in range(6):
            IV = randint(0,31)
            self.IVS.append(IV)

        # Apply all context specfic attribute alterations
        if context == "Trainer":
            self.setTrainerEVs()

        # Sets "adjusted" stats and give the pokemon its starting moveset
        self.calculateAdjustedStats()
        # self.actualStats = self.adjustedStats()
        self.determineStartMoveset()
    

    def copyBaseValues(self,speciesID):
        # Open File and splits each line into a list at " "s
        statsFilePath = selectFile(["DataTables"],"full_pokemonData.txt")
        statsFile = readFile(statsFilePath, " ")
        
        
        

    # Prints pokemons stats to terminal.
    def printStats(self):
        print(f"Species: {self.species} of nature {self.nature}")
        print(f"Typing: {self.types[0]}  {self.types[1]} ")
        print(f"Lvl: {self.level} from Exp: {self.experience} ")
        print(f"Base Stats: HP:{self.baseStats[0]}  ATK:{self.baseStats[1]} DEF:{self.baseStats[2]} SPA:{self.baseStats[3]} SPD:{self.baseStats[4]} SPE:{self.baseStats[5]}")
        print(f"IVs: HP:{self.IVs[0]} ATK:{self.IVs[1]} DEF:{self.IVs[2]} SPA:{self.IVs[3]} SPD:{self.IVs[4]} SPE:{self.IVs[5]}")
        print(f"EVs: HP:{self.EVs[0]} ATK:{self.EVs[1]} DEF:{self.EVs[2]} SPA:{self.EVs[3]} SPD:{self.EVs[4]} SPE:{self.EVs[5]}")
        print(f"Adjusted Stats: HP:{self.adjustedStats[0]} ATK:{self.adjustedStats[1]} DEF:{self.adjustedStats[2]} SPA:{self.adjustedStats[3]} SPD:{self.adjustedStats[4]} SPE:{self.adjustedStats[5]}")
    

    # Picks a random nature and assigns correct multipliers from the pokemon_natures dictonary
    def assignRandomNature(self):
        natureID = randint(1,25)
        natureInfo = pokemon_natures[natureID]
        self.nature = natureInfo[0]
        self.natureMultipliers = [1,1,1,1,1,1]
        self.natureMultipliers[natureInfo[1] - 1] = 1.1
        self.natureMultipliers[natureInfo[2] - 1] = 0.9
        

    # Calculate stats adjusted for Lvl, IVs, EVs and nature
    def calculateAdjustedStats(self):
        self.adjustedStats = []
        isHP = True
        statID = 0
        for each in self.baseStats:
            lvlAdjustedStat = calculateStat(int(self.baseStats[statID]),self.level,self.IVs[statID],self.EVs[statID],isHP,self.natureMultipliers[statID])
            self.adjustedStats.append(lvlAdjustedStat)
            statID += 1
            isHP = False


    # Just increase the pokemons experience by a given amount and runs levelUp check
    def addExperience(self,newExperience):
        self.experience += newExperience
        self.levelUp()


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
    
    # Test Functions, will be removed later.
    # Allows adding experience amounts to check the pokemon is leveling up appropriatley
    def testLeveling(self):
        while True:  
            try:
                experienceAdd  = int(input("Add Experience: \n> "))
                self.experience += experienceAdd
                self.levelUp()
            except:
                break



# Test Functions to check stuff is working correctly
# Generates random Test pokemon to check pokemon generation is working
def generateTestPokemon(amount,minLvl,maxLvl):
    for i in range(0,amount):
        mypokemon = pokemon(randint(1,721),minLvl,maxLvl,"Wild")
        print(f"Generated Pokemon {i  +  1}")
        mypokemon.printStats()
        print("-----------------------------------------------")
        # mypokemon.testLeveling()
        
# generateTestPokemon(1000,1,1)
