import os 
import csv
# Using CSV formats textfiles how I normally do, but has useful built-in functions

def getPath(fileName):
    filePath = os.path.join(format(os.getcwd()), fileName)
    return filePath

file = getPath("testFile.txt")
with open(file, 'w', newline = "") as csvfile:
    employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

