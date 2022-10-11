# Need to compile all useful information into one file, rather than consulting several different files.
# I assume this will be slower, but it'll be easier to keep track of for the time being.
import os
import csv
from fileControl import *

# Specificaly for rearranging the evolutions data
# Had to write on Codio as the Uni PC did not have a python intepreter for some reason
def reOrderEvolution():
    evolutionsPath = selectFile(["ProjectDataCleaning","cleanedData"], "evolutionChains.txt")
    evolutionLines = readFile(evolutionsPath)
    print(f"Before: \n {evolutionLines}")

    # Take each line and then add the correct evolutions
    for line in range(1, len(evolutionLines)):
        if evolutionLines[line][2] != "":
            evolvesFrom = int(evolutionLines[line][2])
            evolutionLines[evolvesFrom].append(evolutionLines[line][0])

    # Adds missing coloumn to those species who do not evolve
    for line in range(1, len(evolutionLines)):
        if len(evolutionLines[line]) < 4:
            evolutionLines[line].append("")

    print(f"After: \n {evolutionLines}")
    writeFile(evolutionsPath, evolutionLines)


# Combines the columns of different csv files, lists keep1 and keep2 ,specify which colums to keep from each file
# File2 will be esentially appended to file1 minus any unwanted lines
def combineFiles(file1, file2, keep1, keep2):
    # Open repective files
    file1Path = selectFile(["ProjectDataCleaning","cleanedData"], file1)
    file2Path = selectFile(["ProjectDataCleaning","cleanedData"], file2)
    file1Lines = readFile(file1Path)
    file2Lines = readFile(file2Path)
    newLines = []
    lineID = 0
    
    for line in file1Lines:
        newLine = []

        # Adds all desired columns from file 1
        for item in keep1:
            newLine.append(file1Lines[lineID][item])
        
        # Adds all desired columns from file 2
        for item in keep2:
            newLine.append(file2Lines[lineID][item])

        newLines.append(newLine)
        lineID += 1
    
    writeFile(file1Path, newLines)


combineFiles("pokemon.txt","evolutionChains.txt",[0,1,2,3,4,5,6,7,8,9,10,11],[2,3])