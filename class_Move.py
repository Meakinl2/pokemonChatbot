from ProjectDataCleaning.fileControl import *
from dictonaries import *

# Assigns all realted information to a move, for a given pokemon.
class Move:
    def __init__(self,moveName):
        movesFile = selectFile(["DataTables"],"full_move_data.txt")
        moveFileLines = readFile(movesFile,"\t")
        for line in moveFileLines:
            if moveName in line:
                moveInformation = line


        # As I am using two different sources for moves and pokemon, sometimes names don't quite line up
        # I will look for a better solution, but this will help for now.
        try: 
            self.name = moveName
            self.moveID = moveInformation[0]
            self.typing = type_IDs[int(moveInformation[5]) + 1]
            self.pp = int(moveInformation[10])
            self.priority = int(moveInformation[11])
            self.damageClass = move_damage_classes[int(moveInformation[7]) + 1]
            self.critStage = int(moveInformation[19])
        except UnboundLocalError:
                print(f"Error. {moveName} could not be found.")
                exit()

        # Some boxes are blank in the table and so this assign appropriate integer values in their place
        try: 
            self.power = int(moveInformation[8])
        except ValueError:
            self.power = 0

        try: 
            self.accuracy = int(moveInformation[9])
        except  ValueError:
            self.accuracy = 100

        try: 
            self.hitAmount = [int(moveInformation[12]),int(moveInformation[13])]
        except ValueError:
            self.hitAmount = [1,1]

        try:
            self.turnAmount = [int(moveInformation[17]),int(moveInformation[18])]
        except ValueError:
            self.turnAmount = [1,1]



    # Prints move values to terminal, mainly just for checkin geverythin is working
    def printMoveValues(self):
        print(f"Move ID: {self.moveID}")
        print(f"Move Name: {self.name}")
        print(f"Typing: {self.typing}")
        print(f"Damage Class: {self.damageClass}")
        print(f"Power: {self.power}")
        print(f"Hit No.: {self.hitAmount[0]}-{self.hitAmount[1]}")
        print(f"Turn No.: {self.turnAmount[0]}-{self.turnAmount[1]}")
        print(f"PP: {self.pp}")
        print(f"Accuracy: {self.accuracy}")
        print(f"Priority: {self.priority}")


    # End of Move Class
    