# As I can't find evolution data in a form that I can use, I will generate appropriate bounds for all evolvable pokemon
# These will not accurately match the main series and will likely be changed later on if I have extra time
# They will however suffice as a basic system to allow me to move on to other aspects of the game

from fileControl import *

# Creates a file that provides a list of all species on the same evolution chain.
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
            
    evolutionChainsFile = selectFile(["ProjectDataCleaning","CleanedData"],"evolutionChains.txt")
    writeFile(evolutionChainsFile, evolutionChainsLines)

generateEvolutionChains()