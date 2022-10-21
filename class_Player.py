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
        self.party.append(Pokemon(starterID,5,5,"Player",self.uniqueID))
        self.party[0].nickname = nickname
        self.party[0].picklePokemonObject()



    # Creates the Unique ID for identifing a specific Player class instance
    def createUniqueID(self):
        playerCodesPath = os.path.join(format(os.getcwd()),"SavedObjects","PlayerInstances","player_instance_codes.txt")
        self.uniqueID = generateUniqueReference(playerCodesPath)


    # Creates a new Folder in the pokemon Storage Folder for all of pokemon belonging to this player instance
    def createStorageFolder(self):
        playerPokemonStorage = os.path.join(format(os.getcwd()),"SavedObjects","PokemonStorage",self.uniqueID)
        if not os.path.exists(playerPokemonStorage):
            os.makedirs(playerPokemonStorage)
            

    # Pickles pokemon data to the relevant file adn directory
    # This also saves all data for the pokemon in the the players party, which is rather handy
    def picklePlayerObject(self):
        playerPicklePath = os.path.join(format(os.getcwd()),"SavedObjects","PlayerInstances",self.uniqueID)
        if not os.path.exists(playerPicklePath):
            with open(playerPicklePath,"x") as file:
                file.close()
        with open(playerPicklePath,"wb") as pickleFile:
            pickle.dump(self,pickleFile)
            pickleFile.close()
        

    # Swaps the position of two pokemon in the party, mainly so position 0 can be the party leader
    def reorderParty(self,swapFrom,swapTo):
        index1 = self.party.index(swapFrom)
        index2 = self.party.index(swapTo)
        temp = self.party[index1]
        self.party[index1] = self.party[index2]
        self.party[index2] = temp

        

    def moveToParty(self):
        pass


    def moveToStorage(self):
        pass
        
    # Adds a new pokemon to the players party or to their storage if party is full
    # Also changes relevant attributes and datasets to refelct this
    def captureNewPokemon(self,pokemon):
        pokemon.owner = self.uniqueID
        pokemon.context = "Player"
        if len(self.party) < 6:
            self.party.append(pokemon)
        pokemonInstancesPath = os.path.join(format(os.getcwd()),"SavedObjects","PokemonStorage","pokemon_instance_codes.txt")
        pokemon.uniqueID = generateUniqueReference(pokemonInstancesPath)
        pokemon.picklePokemonObject()


    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Unique ID: {self.uniqueID}")
        print(f"Money: {self.money}")
        print(f"Current Party: ")
        for pokemon in self.party:
            print(f" - {pokemon.nickname} the Lvl {pokemon.level} {pokemon.species} ")


    # Test Functions


    # End of Player class
