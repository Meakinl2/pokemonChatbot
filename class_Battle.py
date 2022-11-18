import random

from ProjectDataCleaning.fileControl import *
from dictonaries import *
from other_functions import *
import user_inputs

class Battle:
    def __init__(self,player,opponent,battleType):
        self.player = player
        self.opponent = opponent
                
        maxActive = {"1v1": 1,"2v2": 2,"3v3": 3,"Wild": 1}

        self.playerActive = []
        for i in range(0,len(player.party)):
            if not player.party[i].isFainted and len(self.playerActive) < maxActive[battleType]:
                player.party[i].isActive = True
                self.playerActive.append(i)
                
        self.opponentActive = []
        for i in range(0,maxActive[battleType]):
            opponent.party[i].isActive = True
            self.opponentActive.append(i)
            
        print(f"\nYou are approached by {self.opponent.title} {self.opponent.name}.")
        print(f"\n{self.opponent.title} {self.opponent.name} sends out {self.opponent.party[self.opponentActive[0]].nickname}.")
        print(f"Go, {self.player.party[self.playerActive[0]].nickname}.")

        self.battleLoop()
        
    # --------------------------------------------------------------

    # Functions that run during the course of the battle

    # The basic battle loop that runs every turn
    def battleLoop(self):
        self.battleOngoing = True
        turn = 0
        while self.battleOngoing:
            turn += 1
            print("----------------------------------------------------------") 
            print(f"Turn {turn}")

            for i in range(len(self.playerActive)):
                self.player.party[self.playerActive[i]].turnAction = user_inputs.userBattleMain(self.player,self.playerActive[i],self.playerActive,self.opponent,self.opponentActive)

            for i in range(len(self.opponentActive)):
                self.opponent.party[self.opponentActive[i]].turnAction = self.opponent.battleTurn(self.opponent.party[self.opponentActive[i]],self.opponentActive,self.playerActive)
            
            self.determineActionOrder()
            
            # Executes all currently items in the action queue, different funnctions called for different action types
            for i in range(len(self.actionQueue)):
                pokemon = self.actionQueue[i][0]
                action = self.actionQueue[i][0].turnAction
                if action[2] == "Move":
                    self.useMove(pokemon,action)
                elif action[2] == "Item":
                    self.useItem(pokemon,action)
                elif action[2] == "Switch":
                    self.switchOut(action)
                elif action[2] == "Flee":
                    self.checkFleeBattle(pokemon)

            switch_in = self.pokemonUnconcious(self.playerActive,self.player)
            if switch_in not in ["Blackout",None]:
                print(f"Go, {self.player.party[switch_in].nickname}.")
            elif switch_in == "Blackout":
                self.defeat("Blackout")

            switch_in = self.pokemonUnconcious(self.opponentActive,self.opponent)
            if switch_in not in ["Blackout",None]:
                print(f"Opponent sends out {self.opponent.party[switch_in].nickname}.")
            elif switch_in == "Blackout":
                self.victory("Blackout")

            self.endBattle()

    # Checks if any active pokemon become unconcious and then prompts the correct side for a switch in
    def pokemonUnconcious(self,active_list,trainer):
        for active_pokemon in active_list:
            pokemon = trainer.party[active_pokemon]
            if pokemon.actualStats[0] <= 0:
                print(f"{pokemon.nickname} has fainted.")
                pokemon.isFainted = True
                pokemon.isActive = False
                remaining_pokemon = False
                for pokemon in trainer.party:
                    if not pokemon.isFainted:
                        remaining_pokemon = True

                if remaining_pokemon:
                    switch_in = trainer.pokemonFainted(active_list)
                    trainer.party[switch_in].isActive = True
                    active_list[active_list.index(active_pokemon)] = switch_in
                    return switch_in
                else:
                    return "Blackout"

    # Determines in what order each action should occur.
    def determineActionOrder(self):
        self.actionQueue = []
        priorityLevels = {"Item":1,"Switch":2,"Flee":3}
        
        # Assing priority for type of action and move priority level
        allActiveActions = []
        for index in self.playerActive:
            allActiveActions.append(self.player.party[index])

        for index in self.opponentActive:
            allActiveActions.append(self.opponent.party[index])
  
        for pokemon in allActiveActions:
            if pokemon.turnAction[2] == "Move":
                priority = pokemon.knownMoves[pokemon.turnAction[3]].priority
                priority += pokemon.actualStats[5]

            else:
                priority = 1000 + priorityLevels[pokemon.turnAction[2]]
            action = [pokemon,priority]
            self.actionQueue.append(action)
        
        
        # Reorders moves based on priority, it is bubble sort and it is very inefficent, but there will be six items max, so it's good enough
        ordered = False
        while not ordered:
            moves = 0
            for i in range(1,len(self.actionQueue)):
                if self.actionQueue[i][1] > self.actionQueue[i - 1][1]:
                    temp = self.actionQueue[i]
                    self.actionQueue[i] = self.actionQueue[i - 1]
                    self.actionQueue[i - 1] = temp
                    moves += 1

            if moves == 0:
                ordered = True


    # Use a named move an inflicts relavant effects
    def useMove(self,pokemon,action):
        if action[4] == "Player":
            target = self.player.party[self.playerActive[action[5]]]
        elif action[4] == "Opponent":
            target = self.opponent.party[self.opponentActive[action[5]]]
        
        move = pokemon.knownMoves[action[3]]
        move.pp -= 1

        print(f"\n{pokemon.nickname} used {pokemon.knownMoves[action[3]].name} on {target.nickname}.")

        # TODO Add in chance to miss
        


        moveDamage,appliedMultipliers = calculateDamage(pokemon,target,move)
        if moveDamage ==  0 and "Nullified" not in appliedMultipliers and move.damageClass != "Status":
            moveDamage = 1

        target.actualStats[0] -= moveDamage
        if target.actualStats[0] < 0:
            target.actualStats[0] = 0
        
        
        print(f"{target.nickname} took {moveDamage} damage and now has {target.actualStats[0]}/{target.adjustedStats[0]}")

        if "Nullified" in appliedMultipliers:
            print("It had no effect.")
        elif "Supereffective" in appliedMultipliers and "Ineffective" not in appliedMultipliers:
            print("It was Supereffective.")
        elif "Uneffective" in appliedMultipliers and "Supereffective" not in appliedMultipliers:
            print("It wasn't very effective.")

        if "Critical" in appliedMultipliers:
            print("It was a Critical Hit.")

    def useItem(self):
        print("Item")

    # Use a specified item and inflict 
    def usePotion(self,pokemon,action):
        print("Potion")

    def userPokeball(self,pokemon,action):
        print("Pokeball")

    # Switches out to a desired Pokemon
    def switchOut(self,action):
        if action[0] == "Player":
            index = self.playerActive.index(action[1])
            self.playerActive[index] = action[3]
        elif action[0] == "Opponent":
            index = self.opponentActive.index(action[1])
            self.opponentActive[index] = action[3]


    # Checks if a the battle can be fled, and then acts accordingly
    def checkFleeBattle(self,pokemon):
        
        print(f"{pokemon.nickname} attempts to flee.")
        if pokemon.actualStats[5] > self.opponent.party[self.opponentActive[0]].actualStats[5]:
            self.defeat("Flee")
            print(f"{pokemon.nickname} got away.")
        else:
            print(f"{pokemon.nickname} did not escape.")


    # --------------------------------------------------------------

    # Functions that run at the end of the battle

    def victory(self,reason):

        if reason == "Blackout":
            print(f"{self.opponent.title} {self.opponent.name} has no more pokemon left.")
            
            total_score = 0
            party_size = 0
            for pokemon in self.player.party:
                total_score += pokemon.level
                party_size += 1

            payout = (base_payout[total_score % 10 * party_size] * random.randint(-30,30) / 100) // 1
            print(f"You win {payout}₽")
            self.player.money += payout

        if reason == "Capture":
            print("Capture")
        
        self.player.picklePlayerObject()
        self.battleOngoing = False



    def defeat(self,reason):
        if reason ==  "Blackout":
            print("You have no more Pokémon that can fight.")



        elif reason == "Flee":
            print("You managed to successfully flee.")
        
        else:
            print("You have lost!")
        self.battleOngoing = False

    

