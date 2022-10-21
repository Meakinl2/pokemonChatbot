# Generates the oppposing trainers for battles
# At first, they will just be random at an approximated strength
# Might add more stuff later on to refine the process

import os
from math import sqrt
from random import randint

from ProjectDataCleaning.fileControl import *
from class_Pokemon import Pokemon
from dictonaries import *

class Trainer:
    def __init__(self,opponent):
        self.title = "Trainer"
        self.name = "Dummy"
        self.opponent = opponent
        self.party = []

        self.determinePartySize()
        self.trainerPokemonLevel()
        self.generateParty()

    
    # Makes Trainer party length similar to that of the opponent that is being faced
    def determinePartySize(self):
        self.partySize = len(self.opponent.party) + randint(-1,1)
        if self.partySize > 6:
            self.partySize = 6
        if self.partySize < 1:
            self.partySize = 1


    # Makes trainers pokemon a level that should make the fight relatively fair, definetley room for improvent though
    def trainerPokemonLevel(self):
        totalPlayerScore =  0
        for pokemon in self.opponent.party:
            totalPlayerScore += pokemon.level ** 2
        self.baseLvl = sqrt(totalPlayerScore / self.partySize) // 1


    # Generate a random party for the trainer, that is relatively well balanced level-wise with the player
    def generateParty(self):
        available_species_path = selectFile(["DataTables"],"available_species.txt")
        availableSpecies = readFile(available_species_path," ")

        minLvl = int(self.baseLvl - 3 - (self.baseLvl * 0.1) // 1)
        maxLvl = int(self.baseLvl + 3 + (self.baseLvl * 0.1) // 1)
        for i in range(self.partySize):
            item = randint(0,len(availableSpecies)-1)
            chosenSpecies = availableSpecies[item][0]
            self.party.append(Pokemon(chosenSpecies,minLvl,maxLvl,"Trainer"))

    def battleTurn(self,opponentParty):
        pass


    # Just print relevant information about the trainers attributes
    def printPartyStats(self):
        print(f"{self.title} {self.name}")
        print("Party: ")
        for pokemon in self.party:
            stats = pokemon.actualStats
            moves = pokemon.knownMoves
            print("--------------------------------------------------")
            print(f" > Lvl {pokemon.level} {pokemon.species}")
            print(f"   Typing: {pokemon.types[0]} {pokemon.types[1]}")
            print(f"   Health: {pokemon.actualStats[0]}/{pokemon.adjustedStats[0]}")
            print(f"   Stats: ATK:{stats[1]} DEF:{stats[2]} SPA:{stats[3]} SPD:{stats[4]} SPE:{stats[5]}")
            print(f"   Available Moves: ")
            for move in moves:
                print(f"     - {move.name}")
            
    
