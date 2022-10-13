# As I can't find evolution data in a form that I can use, I will generate appropriate bounds for all evolvable pokemon
# These will not accurately match the main series and will likely be changed later on if I have extra time
# They will however suffice as a basic system to allow me to move on to other aspects of the game

from random import randint
from fileControl import *

# Creates a file that provides a list of all species on the same evolution chain.
# This does have the issue of repeats where some pokemon have multiple evolutions, 
# They are few in number and can be handled as special cases and processed individaully
def generateEvolutionChains():
    evolutionsFile = selectFile(["ProjectDataCleaning","CleanedData"],"evolutions.txt")
    evolutionsLines = readFile(evolutionsFile)
    evolutionChainsLines = []
    categorizedSpecies = []

    # Cycles through all species
    for species in range(1,len(evolutionsLines)):
        baseSpeciesFound = False
        chainCompleted = False

        newChainLine = []
        if int(species) not in (categorizedSpecies):
           
           # Finds the base (first) evolution in each chain
            while not baseSpeciesFound:
                if evolutionsLines[int(species)][2] == "":
                    baseSpeciesFound = True
                    newChainLine.append(int(species))
                    categorizedSpecies.append(int(species))
                else:
                    species = evolutionsLines[int(species)][2]
            
            # Goes up the chain adding each item to a list until end of the chain is reached
            while not chainCompleted:
                if evolutionsLines[int(species)][3] == "":
                    chainCompleted = True 
                else:
                    species = evolutionsLines[int(species)][3]
                    newChainLine.append(int(species))
                    categorizedSpecies.append(int(species))
                    
            evolutionChainsLines.append(newChainLine)
    
    # Write data to new File, for later use
    evolutionChainsFile = selectFile(["ProjectDataCleaning","CleanedData"],"evolutionChains.txt")
    writeFile(evolutionChainsFile, evolutionChainsLines)

# generateEvolutionChains()

# Assigns the level bounds at which each evolution occurs
# They are pretty much random, might make it player changeable.
def generateEvolutionBounds():
    evolutionChainsFile = selectFile(["ProjectDataCleaning","CleanedData"],"evolutionChains.txt")
    evolutionChainsLines = readFile(evolutionChainsFile)
    pokemonFile = selectFile(["DataTables"],"pokemonBaseStats.txt")
    pokemonLines = readFile(pokemonFile)
    
    for chain in evolutionChainsLines:
        if len(chain) == 1:
            pokemonLines[int(chain[0])].append("")
        elif len(chain) == 2:
            evolutionBound = randint(25,61)
            pokemonLines[int(chain[0])].append(evolutionBound)

        elif len(chain) == 3:
            evolutionBound1 = randint(16,31)
            evolutionBound2 = randint(45,71)
            pokemonLines[int(chain[0])].append(evolutionBound1)
            pokemonLines[int(chain[1])].append(evolutionBound2)
        
    writeFile(pokemonFile,pokemonLines)

# generateEvolutionBounds()