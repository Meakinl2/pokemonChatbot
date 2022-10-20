from ProjectDataCleaning.fileControl import *
from dictonaries import *

# Assigns all realted information to a move, for a given pokemon.
class Move:
    def __init__(self,moveName):
        movesFile  = selectFile(["DataTables"],"moveInformation.txt")
        moveFileLines = readFile(movesFile,",")
        for line in moveFileLines:
            if moveName in line:
                moveInformation = line

        self.name = moveName
        self.moveID = moveInformation[0]
        self.typing = type_IDs[int(moveInformation[2])]
        self.pp = int(moveInformation[4])
        self.priority = int(moveInformation[6])
        self.damageClass = move_damage_classes[int(moveInformation[8])]
        self.baseCritStage = int(moveInformation[19])

        # Some boxes are blank in the table and so this assign appropriate integer values in their place
        try: 
            self.power = int(moveInformation[3])
        except ValueError:
            self.power = 0

        try: 
            self.accuracy = int(moveInformation[5])
        except  ValueError:
            self.accuracy = 100

        try: 
            self.hitAmount = [int(moveInformation[13]),int(moveInformation[14])]
        except ValueError:
            self.hitAmount = [1,1]

        try:
            self.turnAmount = [int(moveInformation[15]),int(moveInformation[16])]
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
    