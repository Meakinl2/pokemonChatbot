# This just contains the functions that I rewrote or scrapped completely following their inital completion
# Might not work as ajoining functions may also have been rewritten
# A lot of the inital ones are because I discovered the csv library


# From ProjectDataCleaning\fileControl.py

# Redone as csv library used to make some steps redundant
# Opens and reads a given file, so that the data can be manipulated
def readFile(filePath):
   print(filePath)
   with open(filePath, 'r') as file:
      fileLines = file.readlines()
      file.close()
   for line in fileLines:
      line = line[:-2]
   return fileLines

# Redone as csv library used to make some steps redundant
# Writes new lines to the corerct file
def writeFile(filePath, fileLines):
   file = open(filePath, "w")
   for item in fileLines:
      item = item[:-1]
      file.writelines(item + "\n")

# From ProjectDataCleaning\cleaning.py

# Almost whole thing made redundant by csv library
# Will split each line of file into a list, will keep all elements in the list keepElements
def cleanData(rawLineStrings, keepItems):
   rawLineLists = []
   
   for line in rawLineStrings:
      line = line.split(",")
      
      rawLineLists.append(line)
   
   cleanLineStrings = []
   
   for line in rawLineLists:
      cleanLine = []
      cleanString = ''
      for item in keepItems:
         cleanLine.append(line[item])

      for item in cleanLine:
         cleanString = f"{cleanString}{item},"
              
      cleanLineStrings.append(cleanString)
   
   return cleanLineStrings