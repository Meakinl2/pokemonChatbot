# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

from ProjectDataCleaning.fileControl import *
import os,random,pickle
from class_Player import Player
from class_Trainer import Trainer
from class_Battle import Battle


pickleFilePath = selectFile(["SavedObjects","PlayerInstances"],"WJD6K0E4TT")
with open(pickleFilePath, "rb") as pickleFile:
    pickleInfo = pickleFile.read()
    pickleFile.close()
    
player = pickle.loads(pickleInfo)

for pokemon in player.party:
    pokemon.resetBattleValues()

trainer = Trainer(player)

Battle(player,trainer,"1v1")


