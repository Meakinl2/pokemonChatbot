# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

import os,random,pickle,math,numpy

from ProjectDataCleaning.fileControl import *
from input_interpretation import *
from class_Main import *
from class_Player import Player
from class_Trainer import Trainer
from class_Battle import Battle

def testBattle(playerCode):
    pickleFilePath = selectFile(["SavedObjects","PlayerInstances"],playerCode)
    with open(pickleFilePath, "rb") as pickleFile:
        pickleInfo = pickleFile.read()
        pickleFile.close()
        
    player = pickle.loads(pickleInfo)

    for pokemon in player.party:
        pokemon.resetBattleValues()

    trainer = Trainer(player)

    print(f"\nTrainer: {trainer.title} {trainer.name}")
    print(f"Party:")
    for pokemon in trainer.party:
        print(f"\n - Lvl {pokemon.level} {pokemon.species}")
        for move in pokemon.knownMoves:
            print(f"   > {move.name}")

    Battle(player,trainer,"1v1")

# Main()
testBattle("XK484TPH5U")
# Player()

exit()
