
import csv

listUserId = []

def exist(theID):
    return theID in listUserId


with open("Dataset/datasetFinal.csv", 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='"')

    with open('Dataset/test/UserID.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 1
        newRow = [0,0]
        k = 1
        for row in spamreader:
            k += 1
            if k % 100 == 0:
                print(k)
            if not exist(row[0]):
                listUserId.append(row[0])
                newRow[0], newRow[1] = i, row[0]
                i += 1
                spamwriter.writerow(newRow)
