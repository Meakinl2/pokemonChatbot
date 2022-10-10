import os 
import csv

def getPath(fileName):
    filePath = os.path.join(format(os.getcwd()), fileName)
    return filePath

file = getPath("testFile.txt")
with open(file, 'w', newline = "") as csvfile:
    employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


"I would like to use Double Punch on Enemy1"
"Enemy1 Double Punch"