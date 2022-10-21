import os
import pickle 
from ProjectDataCleaning.fileControl import *
from class_Pokemon import Pokemon
import user_inputs

class Player:
    def __init__(self):
        self.createUniqueID()
        self.createStorageFolder()
        self.money = 0
        self.inventory = {}
        self.party = []

        user_inputs.pickPlayerName(self)
        starterID, nickname = user_inputs.pickStartingPokemon(self)
        self.party.append(Pokemon(starterID,5,5,"Player"))
        self.party[0].nickname = nickname

        self.picklePlayerObject()


    # Creates the Unique ID for identifing a specific Player class instance
    def createUniqueID(self):
        playerCodesPath = os.path.join(format(os.getcwd()),"SavedObjects","PlayerInstances","player_instance_codes.txt")
        self.uniqueID = generateUniqueReference(playerCodesPath)


    # Creates a new Folder in the pokemon Storage Folder for all of pokemon belonging to this player instance
    def createStorageFolder(self):
        playerPokemonStorage = os.path.join(format(os.getcwd()),"SavedObjects","PokemonStorage",self.uniqueID)
        fullCodeFilePath = os.path.join(playerPokemonStorage, "pokemon_instance_codes.txt")
        print(fullCodeFilePath)
        if not os.path.exists(playerPokemonStorage):
            os.makedirs(playerPokemonStorage)
            with open(fullCodeFilePath,"x") as file:
                file.close()

    # Pickles pokemon data to the relevant file adn directory
    def picklePlayerObject(self):
        playerPicklePath = os.path.join(format(os.getcwd()),"SavedObjects","PlayerInstances",self.uniqueID)
        if not os.path.exists(playerPicklePath):
            with open(playerPicklePath,"x") as file:
                file.close()
        with open(playerPicklePath,"wb") as pickleFile:
            pickle.dump(self,pickleFile)
            pickleFile.close()
        

    def reorderParty():
        pass


    def moveToParty(self):
        pass


    def moveToStorage(self):
        pass
        

    def captureNewPokemon(self,pokemon):
        pokemon.owner = self.uniqueID
        if len(self.party) < 6:
            pokemon.context = "Player"
            self.party.append(pokemon)
        else:
            pass
            

    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Unique ID: {self.uniqueID}")
        print(f"Money: {self.money}")
        print(f"Current Party: ")
        for pokemon in self.party:
            print(f" - {pokemon.nickname} the Lvl {pokemon.level} {pokemon.species} ")




    # Test Functions


    # End of Player class


player = Player()
player.printStats()
