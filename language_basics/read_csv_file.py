def readHeaderFromFile(filename):
    #datafile = open(filename, "r")
    #headers=[]
    #for line in datafile:
    #    entry = line.strip().split(";")
    #    #print(entry);
    #    if entry[0] == "Anz_Kunden":
    #        headers = entry
    #        return headers;
    return ["Anz_Kunden", "Gesamtkosten"]

def readDatasetsFromFile(filename):
    dataset = []
    datafile = open(filename, "r")
    for line in datafile:
        entry = line.strip().split(";")
        #print(entry);
        result = []
        if entry[0] == "Anz_Kunden":
            continue
        else:
            result.append(int(entry[0]))
            #result.append(float(entry[1].replace(",",".")))
            #result.append(int(entry[2]))
            #result.append(float(entry[3].replace(",",".")))
            #result.append(int(entry[4]))
            #result.append(float(entry[5].replace(",",".")))
            result.append(float(entry[6].replace(",",".")))
            dataset.append(result)
    return dataset

def findEntry(dataset, i):
    for e in dataset:
        if e[0] == i:
            return e
    return "not found"

def getCost(dataset, i):
    e = findEntry(dataset, i)
    return e[1]

FILENAME = "data.csv"
headers = readHeaderFromFile(FILENAME)
dataset = readDatasetsFromFile(FILENAME)


print(headers)
#print(findEntry(dataset, 36))
#print(dataset)
#for i in dataset:
#    s = ""
#    for e in i:
#        s = s + str(e) + "\t"
#    print(s)

for i in range(10, 20):
    print(str(i) + "\t" + str(getCost(dataset, i)))
    