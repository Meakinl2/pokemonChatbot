
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
            for item in speciesData:
                print(item)
    except IndexError:
        pass


