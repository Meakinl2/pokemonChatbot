import os
import csv
import random

# Finds full path of a given file in a given folder, was having trouble with it not reading the correct path, ended up with a slightly different method than I normally use.
# I might rewrite this, I am unsure if it is better like this or not
def selectFile(folders,fileName):
   folderPath = format(os.getcwd())
   for folder in folders:
      folderPath = os.path.join(folderPath,folder)
   filePath = os.path.join(folderPath,fileName)
   return filePath


# Opens and reads a given file, so that the data can be manipulated
def readFile(filePath,delim):
   with open(filePath, "r") as csvFile:
        csvReader = csv.reader(csvFile,delimiter = delim)
        fileLines = list(csvReader)
        csvFile.close()
        return fileLines


# Writes new lines to the correct file
def writeFile(filePath,fileLines):
   with open(filePath, "w", newline = "") as csvFile:
        csvWriter = csv.writer(csvFile,delimiter = ",")
        csvWriter.writerows(fileLines)
        csvFile.close()


# Generates a unique string of length 10 to identify pokemon and player objects
# There is absolutely no need for it to be done this way, I just prefer it to straight up numbering them
# This function took way to long to make work, I'll put that down to it being 1:20 in the morning
def generateUniqueReference(existing_instances_path):
   with open(existing_instances_path,"r") as file:
      existingInstances = file.readlines()
      file.close()
   
   uniqueString = False
   while not uniqueString:
      string = ""

      for i in range(10):
         string += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
      string += "\n"

      if string not in existingInstances:
         existingInstances.append(string)
         uniqueString = True
   
   with open(existing_instances_path,"w") as file:
      for line in existingInstances:
         file.writelines(line)
      file.close()

   return string[0:-1]

