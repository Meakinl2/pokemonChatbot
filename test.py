# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

from ProjectDataCleaning.fileControl import *
import os,random,pickle
from class_Player import Player
from class_Trainer import Trainer


pickleFilePath = selectFile(["SavedObjects","PlayerInstances"],"WJD6K0E4TT")
with open(pickleFilePath, "rb") as pickleFile:
    pickleInfo = pickleFile.read()
    pickleFile.close()
    
player = pickle.loads(pickleInfo)


trainer = Trainer(player)
trainer.printPartyStats()



