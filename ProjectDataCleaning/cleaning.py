# As there is only a few documents each function will be specific to each document, just to make it a bit easier 
# Previous Comment is in fact a lie

import os

# Finds full path of a given file in a given folder, was having trouble with it not reading the correct path, ended up with a slightly different method than I normally use.
def selectFile(folders, fileName):
   folderPath = format(os.getcwd())
   for folder in folders:
      folderPath = os.path.join(folderPath, folder)
      print(folderPath)
   filePath = os.path.join(folderPath, fileName)
   print(filePath)
   return filePath


# Opens and reads a given file, so that the data can be manipulated
def readFile(filePath):
   print(filePath)
   file = open(filePath, 'r')
   fileLines = file.readlines()
   file.close()
   for line in fileLines:
      line = line[:-2]
   return fileLines


# Writes new lines to the corerct file
def writeFile(filePath, fileLines):
   file = open(filePath, "w")
   for item in fileLines:
      item = item[:-1]
      file.writelines(item + "\n")
   
   
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

def run(fileName, keepLines): 
   file1 = selectFile(["ProjectDataCleaning","rawData"], fileName)
   rawLines = readFile(file1)
   cleanedLines = cleanData(rawLines, keepLines)
   cleanFile = selectFile(["ProjectDataCleaning","cleanedData"], fileName)
   writeFile(cleanFile, cleanedLines)

run("evolutions.txt", [0,1,3])

