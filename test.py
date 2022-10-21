# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

from ProjectDataCleaning.fileControl import *
import os,random,pickle
from class_Player import *

# player = Player()
# player.picklePlayerObject()

# print("Created New Player")

pickleFilePath = selectFile(["SavedObjects","PlayerInstances"],"WJD6K0E4TT")
with open(pickleFilePath, "rb") as pickleFile:
    pickleInfo = pickleFile.read()
    pickleFile.close()
    
player = pickle.loads(pickleInfo)

pokemon = Pokemon("001",5,5,"Wild")
player.captureNewPokemon(pokemon)

player.printStats()
player.party[0].printStats()
player.party[1].printStats()

with open(pickleFilePath, "wb") as pickleFile:
    pickle.dump(player,pickleFile)
    pickleFile.close()





