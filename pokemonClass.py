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
        print(f"Species ID: {speciesID}")
        self.copyBaseValues(str(speciesID))
        self.nickname = self.species
        self.allowedEvolve = True
        
        # Generate all semi-random attributes
        self.level = randint(minLvl,maxLvl)
        self.experience = levelingBounds[self.level]
        self.assignRandomNature()
        self.EVs = [0,0,0,0,0,0]
        self.IVs = []
        for each in range(6):
            IV = randint(0,31)
            self.IVs.append(IV)

        # Apply all context specfic attribute alterations
        if context == "Trainer":
            self.setTrainerEVs()

        # Sets "adjusted" stats and give the pokemon its starting moveset
        self.calculateAdjustedStats()
        # self.actualStats = self.adjustedStats()
        self.determineStartMoveset()
    
    # Should probably break sections into different functions, just to make it a bit cleaner
    def copyBaseValues(self,speciesID):
        # Open File and splits each line into a list at " "s
        statsFilePath = selectFile(["DataTables"],"full_pokemon_data.txt")
        statsFileLines = readFile(statsFilePath, ",")

        speciesData = []
        line = 0
        # Goes through every line in the document to find the start of the correct entry
        # It is suprisingly fast for 63323 lines
        foundSpecies = False
        while not foundSpecies:
            # New Data has some slight gaps, this if statement will only really be used during testing
            try:
                if statsFileLines[line][0] == speciesID:
                    speciesData.append(statsFileLines[line])
                    foundSpecies = True
            except IndexError:
                pass
            line += 1 

        # Read from the starting line to the end line displayed as "======". 
        fullData = False
        while not fullData:
            line += 1
            try:
                if statsFileLines[line] == ['======']:
                    fullData = True
                else:
                    speciesData.append(statsFileLines[line])
            except IndexError:
                line += 1
                pass
        
        # This is arguably redundant, but I prefer it without the "-"
        for i in range(0,len(speciesData)):
            try:
                speciesData[i].remove("-")
            except ValueError:
                pass

        self.species = speciesData[0][1]
        self.types = [speciesData[6][1]]
        try:
            self.types.append(speciesData[6][3])
        except IndexError:
            self.types.append("")
        self.baseStats = speciesData[1][2].split(".")
        self.evYield = speciesData[2][2].split(".")
        
        # Then we find and assign the pokemons naturally learnt moves.
        self.leveledMoves = []
        collectingMoves = True
        foundStart = False
        foundEnd = False
        i = 0
        while collectingMoves: 
            if foundStart :
                newMove = []
                moveName = ""
                newMove.append(speciesData[i][0])
                for j in range(1,len(speciesData[i])):
                    moveName = moveName + speciesData[i][j]
                newMove.append(moveName)
                self.leveledMoves.append(newMove)
                
            if speciesData[i] == ['Level', 'Up', 'Moves:']:
                foundStart = True

            i += 1
            if speciesData[i] == ['TMs:'] or speciesData[i] == ["Egg","Moves:"]:
                collectingMoves = False

            

        
   
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

    # Prints pokemons stats to terminal.
    def printStats(self):
        print(f"Species: {self.species} of nature {self.nature}")
        print(f"Typing: {self.types[0]}  {self.types[1]} ")
        print(f"Lvl: {self.level} from Exp: {self.experience} ")
        print(f"Base Stats: HP:{self.baseStats[0]}  ATK:{self.baseStats[1]} DEF:{self.baseStats[2]} SPA:{self.baseStats[3]} SPD:{self.baseStats[4]} SPE:{self.baseStats[5]}")
        print(f"IVs: HP:{self.IVs[0]} ATK:{self.IVs[1]} DEF:{self.IVs[2]} SPA:{self.IVs[3]} SPD:{self.IVs[4]} SPE:{self.IVs[5]}")
        print(f"EV Yield: HP:{self.evYield[0]} ATK:{self.evYield[1]} DEF:{self.evYield[2]} SPA:{self.evYield[3]} SPD:{self.evYield[4]} SPE:{self.evYield[5]}")
        print(f"Adjusted Stats: HP:{self.adjustedStats[0]} ATK:{self.adjustedStats[1]} DEF:{self.adjustedStats[2]} SPA:{self.adjustedStats[3]} SPD:{self.adjustedStats[4]} SPE:{self.adjustedStats[5]}")
        print("Learns Naturally, Moves:")
        # print(self.leveledMoves)
        for i in range(0,len(self.leveledMoves)):
            print(f"- {self.leveledMoves[i][1]} at Lvl.{self.leveledMoves[i][0]}")


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
    available_species_path = selectFile(["DataTables"],"available_species.txt")
    availableSpecies = readFile(available_species_path," ")
    for i in range(0,amount):
        item  = randint(0,len(availableSpecies))
        chosenSpecies = availableSpecies[item][0]
        mypokemon = pokemon(chosenSpecies,minLvl,maxLvl,"Wild")
        print(f"Generated Pokemon {i  +  1}")
        mypokemon.printStats()
        print("-----------------------------------------------")
        # mypokemon.testLeveling()
        
generateTestPokemon(1,1,1)
