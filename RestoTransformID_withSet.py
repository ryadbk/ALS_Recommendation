import csv

listUserId = []

with open("Dataset/datasetFinal.csv", 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='"')
    k = 1
    for row in spamreader:
        listUserId.append(row[1])


nbrListe = list(set(listUserId))
print(len(nbrListe))

with open('Dataset/RestoID.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    i = 1
    newRow = [0, 0]
    for row in nbrListe:
        newRow[0], newRow[1] = i, row
        i += 1
        spamwriter.writerow(newRow)