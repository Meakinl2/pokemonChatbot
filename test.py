# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

import os,random,pickle,math,numpy

from ProjectDataCleaning.fileControl import *
from input_interpretation import *
from class_Main import *
from class_Player import Player
from class_Trainer import Trainer
from class_Battle import Battle

def testBattle(player_code):
    pickle_file_path = selectFile(["SavedObjects","PlayerInstances"],player_code)
    with open(pickle_file_path, "rb") as pickle_file:
        pickle_info = pickle_file.read()
        pickle_file.close()
        
    player = pickle.loads(pickle_info)

    player.printStats()

    print("--------------------------------------------")

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


def givePokemon(player_code,pokemon_id):
    pickle_file_path = selectFile(["SavedObjects","PlayerInstances"],player_code)
    with open(pickle_file_path, "rb") as pickle_file:
        pickle_info = pickle_file.read()
        pickle_file.close()
        
    player = pickle.loads(pickle_info)
    player.party.append(Pokemon(pokemon_id,5,5,"Player",player_code))

    player.picklePlayerObject()



# Main()
# Player()
# givePokemon("FS6UF3ADV1","001")
# givePokemon("FS6UF3ADV1","007")

testBattle("FS6UF3ADV1")

pickle_file_path = selectFile(["SavedObjects","PlayerInstances"],"FS6UF3ADV1")
with open(pickle_file_path, "rb") as pickle_file:
    pickle_info = pickle_file.read()
    pickle_file.close()
    
player = pickle.loads(pickle_info)

trainer = Trainer(player)
exit()
