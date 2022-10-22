from ProjectDataCleaning.fileControl import *
from dictonaries import *
from formulae import *

# Not sure if this will be good as a class or not, but it seems like it'll work from my most unexperienced point of view
class battle:
    def __init__(self,player,opponent,battleType):
        self.player = player
        self.opponent = opponent
        
        playerTeam = player.party
        opponentTeam = opponent.party
    
    # Find out what should happen on a given turn, by consulting the player and the opponent AI
    def askTurn(self):
        playerAction = self.player.askTurn()
        opponentAction = self.opponent.askTurn()

        
    def executeTurn(self):
        pass


    def victoryOrDefeat(self):
        pass


    def victory(self):
        pass


    def defeat(self):
        pass

