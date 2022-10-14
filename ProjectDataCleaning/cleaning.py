# As there is only a few documents each function will be specific to each document, just to make it a bit easier 
# Previous Comment is in fact a lie

from fileControl import *

# Removes the coloumns that are unneeded
def cleanData(rawLines, keepItems):
   cleanLines = []
   for rawLine in rawLines:
      cleanLine = []
      for item in keepItems:
         cleanLine.append(rawLine[item])
      cleanLines.append(cleanLine)
   return cleanLines


# Just execute the correct functions in the correct order, completely useless except specifically here
# I will concede that this function is in fact, quite a mess. But what can you do
def run1(fileName, keepLines): 
   print("Reading Lines...")
   file = selectFile(["ProjectDataCleaning","rawData"], fileName)
   rawLines = readFile(file)
   print("Cleaning File...")
   cleanedLines = cleanData(rawLines, keepLines)
   print("Writing to File...")
   cleanFile = selectFile(["ProjectDataCleaning","cleanedData"], fileName)
   writeFile(cleanFile, cleanedLines)
   print("Done.")

run1("moves.txt", [0,1,3,4,5,6,7,8,9,10,11])

# Because the code insists on adding random empty lines, which were not present when I had to run it through codio
# Why this added even more lines I do not know
# I now know.
def removeBlanks(fileLines):
   for line in fileLines:
      if line == ' ':
         fileLines.remove(' ')
   return fileLines


# Another 'beautifully' written hyperspecific function, that I'll never reuse
def run2(fileName):
   file = selectFile(["ProjectDataCleaning","cleanedData"], fileName)
   lines = readFile(file)
   lines = removeBlanks(lines)
   writeFile(file, lines)
   
# run2("evolutions.txt")

# Adds empty elements to csv files to stop Index Errors
def padLines(folders,filename,numPad):
   file = selectFile(folders,filename)
   lines = readFile(file)
   padLines = []

   for line in lines:
      while len(line) < numPad:
         line.append("")
      padLines.append(line)

   writeFile(file,padLines)

# padLines(["DataTables"], "pokemonBaseStats.txt",15)