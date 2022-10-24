from ProjectDataCleaning.fileControl import *
from dictonaries import *
from formulae import *
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
        battleOngoing = True
        while battleOngoing:
            for i in range(len(self.playerActive)):
                self.player.party[self.playerActive[i]].turnAction = user_inputs.userBattleMain(self.player,self.player.party[self.playerActive[i]],self.playerActive,self.opponent,self.opponentActive)

            for i in range(len(self.opponentActive)):
                self.opponent.party[self.opponentActive[i]].turnAction = self.opponent.battleTurn(self.opponent.party[self.opponentActive[i]],self.opponentActive,self.playerActive)
            
            self.determineActionOrder()

            for i in range(len(self.actionQueue)):
                pokemon = self.actionQueue[i][0]
                action = self.actionQueue[i][0].turnAction
                if action[1] == "Move":
                    self.useMove(pokemon,action)
                elif action[1] == "Item":
                    self.useItem(pokemon,action)
                elif action[1] == "Switch":
                    self.switchOut(pokemon,action)
                elif action[1] == "Flee":
                    self.checkFleeBattle()

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
            
            if pokemon.turnAction[1] == "Move":
                priority = pokemon.knownMoves[pokemon.turnAction[2]].priority
                priority += pokemon.actualStats[5]

            else:
                priority = 1000 + priorityLevels[pokemon.turnAction[1]]
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
        if action[3] == "Player":
            target = self.player.party[self.playerActive[action[4]]]
        elif action[3] == "Opponent":
            target = self.opponent.party[self.opponentActive[action[4]]]        
        
        print(f"{pokemon.nickname} used {pokemon.knownMoves[action[2]].name} on {target.nickname}.")


    # Use a specified item and inflict 
    def useItem(self,pokemon,action):
        print(self.actionQueue[0][0].turnAction)
        print("Item")

    # Switches out to a desired Pokemon
    def switchOut(self,pokemon,action):
        print(self.actionQueue[0][0].turnAction)
        print("Switch")

    def checkFleeBattle(self):

        print("Flee")


    # --------------------------------------------------------------

    # Functions that run at the end of the battle

    def victoryOrDefeat(self):
        pass


    def victory(self):
        pass


    def defeat(self):
        pass

