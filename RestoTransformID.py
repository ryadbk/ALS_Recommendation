
import csv

listRestoId = []

def exist(theID):
    return theID in listRestoId

with open("Dataset/datasetFinal.csv", 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='"')

    with open('Dataset/RestoID.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 1
        newRow = [0, 0]
        for row in spamreader:
            if not exist(row[1]):
                listRestoId.append(row[1])
                newRow[0], newRow[1] = i, row[1]
                i += 1
                spamwriter.writerow(newRow)
