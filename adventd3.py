alph = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def parseFile():
    fp = r".\adventd3.txt"
    file = open(fp, "r")
    sacks = file.readlines()
    calcTot(sacks)
    calcTot2(sacks)

def calcTot(sacks):
    tot = 0
    for i in sacks:
        half1 = i[0:int((len(i)/2)):1]
        half2 = i[int((len(i)/2))::1]
        item = [val for val in half1 if val in half2]
        tot += alph.index(item[0]) + 1
    print(tot)

def calcTot2(sacks):
    tot = 0
    for i in range(0,len(sacks),3):
        item = list(set(sacks[i].strip()).intersection(set(sacks[i+1].strip()), set(sacks[i+2].strip())))
        tot += alph.index(item[0]) + 1
    print(tot)
parseFile()
