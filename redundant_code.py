# This just contains the functions that I rewrote or scrapped completely following their inital completion
# Might not work as ajoining functions may also have been rewritten
# A lot of the inital ones are because I discovered the csv library

from ProjectDataCleaning.fileControl import *

# -----------------------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------------------

# From createPokemon.py

# The original function for retrieving basic pokemon information upon creation from file DataTables\PokemonBaseStats.txt
# Upon discovery of the itsjavi github though, more complete data wsas found and was used to replace this old one
# Copying all relevant information from baseStats table
# Used initaily and upon evolution to update relevant attributes
def copyBaseValues(self, speciesID):
   pokemonInfoFile = selectFile(["DataTables"],"pokemonBaseStats.txt")
   pokemonInfo = readFile(pokemonInfoFile)
   speciesInfo = pokemonInfo[speciesID]
      
   self.species = speciesInfo[1]

   try: 
      self.evolveTo = int(speciesInfo[13])
      self.evolveAtLevel = int(speciesInfo[14])
   except:
      self.evolveTo = ""
      self.evolveAtLevel = 1000

   self.baseStats = [int(speciesInfo[5]),int(speciesInfo[6]),int(speciesInfo[7]),int(speciesInfo[8]),int(speciesInfo[9]),int(speciesInfo[10])]
   self.types = [speciesInfo[2],speciesInfo[3]]
      
   if speciesInfo[11] == "true":
      self.isLegendary = True
   else:
      self.isLegendary = False


# The original fuction for evolving before I had full evolution information
# Evolves Pokemon
def evolve(self):
        if self.level >= self.evolveAtLevel and self.allowedEvolve:
            print(f"{self.nickname} is evolving!")
            initalSpecies = self.species
            self.copyBaseValues(self.evolveTo)
            print(f"{self.nickname} evolved in {self.species}")
            if self.nickname == initalSpecies:
                self.nickname = self.species
            self.calculateAdjustedStats()

# -----------------------------------------------------------------------------------------------------

# Code that was purely for testing or changing things to make testing easier

# A fucntion whose entire purpose was to check the typing table was filled out and working correctly. It was.
def checkTypingTable():
   file = selectFile(["DataTables"],"typeDamageMult.txt")
   typingInfo = readFile(file)
   for type1 in range(1,18):
      for type2 in range(1,18):
         print(f"{typingInfo[type1][0]} does {typingInfo[type1][type2]}x damage to {typingInfo[0][type2]}")
         # print(f"{typingInfo[type2][0]} does {typingInfo[type2][type1]}x damage to {typingInfo[0][type1]}")


# Just  a bit of code to bulk out my test player to test some functions.
pickleFilePath = selectFile(["SavedObjects","PlayerInstances"],"WJD6K0E4TT")
with open(pickleFilePath, "rb") as pickleFile:
    pickleInfo = pickleFile.read()
    pickleFile.close()
    
player = pickle.loads(pickleInfo)

pokemon = Pokemon("007",5,5,"Wild")
player.captureNewPokemon(pokemon)

player.printStats()
player.party[0].printStats()
player.party[1].printStats()

with open(pickleFilePath, "wb") as pickleFile:
    pickle.dump(player,pickleFile)
    pickleFile.close()

# -----------------------------------------------------------------------------------------------------

#Mohit code 
# spliting the user input for words
def input_checker(user_party, oppent_party, user_input):
    user_words = user_input.split(" ")
    
# sees if user input matches with the dictonary for moves
    for word in user_words:

        print ("word: " + word)

        for entry in user_party:
            if word.lower() == entry.lower():
                user_words.append(entry)
                print ("\nselected Attacker: " + move)

            for move in user_party[entry]:
                print("move: " + " ". join(map(str,move)))

                if word.lower() == move.lower:
                    user_words.append(move)
                    print("Slected Move: " + move)
                    return move

# sees if user input matches with the dictonary for pokemon

            for animal in user_party:
                if word.lower() == animal.lower():
                    user_words.append(animal)
                    print("\nChosen pokemon: " + pokemon)
                
                for pokemon in user_party[pokemon]:
                    print ("pokenon: " + pokemon)

                    if word.lower() == pokemon.lower:
                        user_words.append(pokemon)
                        print("Selected pokmon: " + " ". join(map(str,pokemon)))
                        return pokemon

# sees if user input matches with the dictonary for oppent pokemon

            for op_pokemon in oppent_party:
                if word.lower() == op_pokemon.lower():
                    user_words.append(op_pokemon)
                    print ("\n oppent pokemon is: " + oppent)

                for oppent in oppent_party[oppent]:
                    print("oppent pokemon: " + oppent)

                    if word.lower() == oppent.lower:
                        user_words.append(oppent)
                        print("Selected oppent pokemon: " + " ". join(map(str,oppent)))