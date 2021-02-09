import csv

listUserId = []


def exist(theID):
    return theID in listUserId


with open("Dataset/UserID.csv", 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='"')

    for row in spamreader:
        listUserId.append(row[1])

    with open('Dataset/datasetFinal.csv', 'r', newline='') as csvfile:
        spamreader2 = csv.reader(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        k=1
        for row in spamreader2:
            if k%1000 == 0 :
                print(k)
            k+=1
            if row[0] not in listUserId:
                print(row[0])
                #throw error
