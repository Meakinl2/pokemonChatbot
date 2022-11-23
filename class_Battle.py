from ProjectDataCleaning.fileControl import *
from dictonaries import *
from formulae import *
import input_interpretation
import user_inputs

# Not sure if this will be good as a class or not, but it seems like it'll work from my most unexperienced point of view
class Battle:
    def __init__(self,player,opponent,battleType):
        self.player = player
        self.opponent = opponent
                
        maxActive = {
            "1v1": 1,
            "2v2": 2,
            "3v3": 3,
            "Wild": 1
        }

        self.playerActive = []
        for i in range(0,len(player.party)):
            if not player.party[i].isFainted and len(self.playerActive) < maxActive[battleType]:
                self.playerActive.append(i)
                
        self.opponentActive = []
        for i in range(0,maxActive[battleType]):
            self.opponentActive.append(i)
    
        self.battleLoop()
        
    # --------------------------------------------------------------

    # Functions that run during the course of the battle

    # The basic battle loop that runs every turn
    def battleLoop(self):
        self.battleOngoing = True
        while self.battleOngoing:
            for i in range(len(self.playerActive)):
                self.player.party[self.playerActive[i]].turnAction = input_interpretation.battleInput(self.player,self.playerActive[i],self.playerActive,self.opponent,self.opponentActive)

            for i in range(len(self.opponentActive)):
                self.opponent.party[self.opponentActive[i]].turnAction = self.opponent.battleTurn(self.opponent.party[self.opponentActive[i]],self.opponentActive,self.playerActive)
            
            self.determineActionOrder()

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

            for activePokemon in self.playerActive:
                if pokemon.actualStats[0] <= 0:
                    print(f"{pokemon.nickname} has fainted.")
                    pokemon.isFainted = True
                    remainingPokemon = False
                    for pokemon in self.playerParty:
                        if pokemon.isFainted == False:
                            remainingPokemon == True

                    if remainingPokemon == True:
                            switchIn = user_inputs.userBattleSelectPokemon(self.player.party)
                            self.playerActive[self.playerActive.index[activePokemon]] = self.player.party[switchIn]


            for pokemon in self.opponentActive:
                if pokemon.actualStats[0] <= 0:
                    pokemon.isFainted = True
                    self.opponent.pokemonFainted() 


            self.endBattle()
        
        self.victoryOrDefeat()

        

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
        print(self.actionQueue[0][0].turnAction)
        
        if action[4] == "Player":
            target = self.player.party[self.playerActive[action[5]]]
        elif action[4] == "Opponent":
            target = self.opponent.party[self.opponentActive[action[5]]]
        
        move = pokemon.knownMoves[action[3]]
        moveDamage,appliedMultipliers = calculateDamage(pokemon,target,move)

        #  To keep in line with regular pokemon
        if moveDamage ==  0 and "Nullified" not in appliedMultipliers and move.damageClass != "Status":
            moveDamage = 1

        target.actualStats[0] -= moveDamage
        if target.actualStats[0] < 0:
            target.actualStats[0] = 0
        
        print(f"{pokemon.nickname} used {pokemon.knownMoves[action[3]].name} on {target.nickname}.")
        print(f"{target.nickname} took {moveDamage} damage and now has {target.actualStats[0]}/{target.adjustedStats[0]}")

        if "Nullified" in appliedMultipliers:
            print("It had no effect.")
        elif "Supereffective" in appliedMultipliers and "Ineffective" not in appliedMultipliers:
            print("It was Supereffective.")
        elif "Uneffective" in appliedMultipliers and "Supereffective" not in appliedMultipliers:
            print("It wasn't very effective.")

        if "Critical" in appliedMultipliers:
            print("It was a Critical Hit.")


    # Use a specified item and inflict 
    def useItem(self,pokemon,action):
        print("Item")


    # Switches out to a desired Pokemon
    def switchOut(self,action):
        if action[0] == "Player":
            index = self.playerActive.index[action[1]]
            self.playerActve[index] = self.player.party[action[3]]
        elif action[0] == "Opponent":
            index = self.opponentActive.index[action[1]]
            self.oppponentActve[index] = self.opponent.party[action[3]]
        print("Switch")


    # Checks if a the battle can be fled, and then acts accordingly
    def checkFleeBattle(self,pokemon):
        self.battleOngoing = False
        print(f"{pokemon.nickname} attempts to flee.")


    # --------------------------------------------------------------

    # Functions that run at the end of the battle

    def endBattle(self):
        pass


    def victoryOrDefeat(self):
        pass


    def victory(self):
        pass


    def defeat(self):
        pass

