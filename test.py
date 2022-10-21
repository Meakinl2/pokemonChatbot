# If this is still in by accident upon submission, know that this is just a file for testing function before they are integrated
# It just makes them a bit easier to work with an cuts down on general clutter. Although I don't really use it all that much.

from ProjectDataCleaning.fileControl import *
import random
import os

with open(os.path.join(format(os.getcwd()),"test.txt"),"r") as file:
    fileLines = file.readlines()


testLines = ["testline1","testline2","testline3","testline4"]
fileLines.append(testLines)

with open(os.path.join(format(os.getcwd()),"test.txt"),"w") as file:
    for line in fileLines:
        file.writelines(line)
    file.close()




