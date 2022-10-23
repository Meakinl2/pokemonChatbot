from ProjectDataCleaning.fileControl import *
from dictonaries import *
from formulae import *
import user_inputs

# Not sure if this will be good as a class or not, but it seems like it'll work from my most unexperienced point of view
class Battle:
    def __init__(self,player,opponent,battleType):
        self.player = player
        self.opponent = opponent
        
        self.playerTeam = player.party
        self.opponentTeam = opponent.party
        
        maxActive = {
            "1v1": 1,
            "2v2": 2,
            "3v3": 3,
            "Wild": 1
        }

        amountActive = 0
        for i in range(0,len(player.party)):
            if not player.party[i].isFainted and amountActive < maxActive[battleType]:
                self.playerActive = [self.playerTeam[i]]
                amountActive += 1
        
        self.opponentActive = []
        for i in range(0,maxActive[battleType]):
            self.opponentActive.append(self.opponentTeam[i])
    
        playerAction = user_inputs.userBattleMain(self.player,self.opponent,self.playerActive[0],self.playerActive,self.opponentActive)
        print(playerAction)
    # --------------------------------------------------------------

    # Functions that run during the course of the battle

    def battleLoop(self):
        pass
    

    # Find out what should happen on a given turn, by consulting the player and the opponent AI
    def askTurn(self):
        playerAction = user_inputs.userBattleMain(self.player,self.opponent,self.playerActive)
        # opponentAction = self.opponent.askTurn()


    def executeTurn(self):
        pass

    # --------------------------------------------------------------

    # Functions that run at the end of the battle

    def victoryOrDefeat(self):
        pass


    def victory(self):
        pass


    def defeat(self):
        pass

