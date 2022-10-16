
from ProjectDataCleaning.fileControl import *

speciesID = "1191"
statsFilePath = selectFile(["DataTables"],"full_pokemon_data.txt")
statsFileLines = readFile(statsFilePath, " ")

speciesData = []
line = 0

# Goes through every line in the document to find the start of the correct entry
# It is suprisingly fast for 63323 lines
foundSpecies = False
while not foundSpecies:
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
        if statsFileLines[line][0] != "======":
            speciesData.append(statsFileLines[line])
        else:
            fullData = True
    except IndexError:
        pass

# This is arguably redundant, but I prefer it without the "-"
for i in range(0,len(speciesData)):
    try:
        speciesData[i].remove("-")
    except ValueError:
        pass

species = speciesData[0][1]
types = [speciesData[7][1]]
try:
    types.append(speciesData[7][3])
except IndexError:
    pass
baseStats = speciesData[2][2].split(".")
evYield = speciesData[3][2].split(".")
naturalMoves = []

print(f"Species ID: {speciesID}")
print(f"Species: {species}")
print(f"Type: {types[0]}   {types[1]}")
print(f"Base Stats: {baseStats}")
print(f"EV Yield: {evYield}")




