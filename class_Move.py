from ProjectDataCleaning.fileControl import *
from dictonaries import *

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


    # Prints move values to terminal, mainly just for checkin geverythin is working
    def printMoveValues(self):
        print(f"Move ID: {self.moveID}")
        print(f"Move Name: {self.name}")
        print(f"Typing: {self.typing}")
        print(f"Damage Class: {self.damageClass}")
        print(f"Power: {self.power}")
        print(f"Hit No.: {self.hitAmount[0]}-{self.hitAmount[1]}")
        print(f"PP: {self.pp}")
        print(f"Accuracy: {self.accuracy}")
        print(f"Priority: {self.priority}")


    # End of Move Class
    
move = Move("Stockpile")
move.printMoveValues


        

