import re

def parseFile():
    fp = r".\adventd4.txt"
    file = open(fp, "r")
    sections = file.readlines()
    calcOverlap(sections)
    calcOverlap2(sections)

def calcOverlap(sections):
    count = 0
    for line in sections:
        line = line.strip()
        temp = re.split(',|-', line)
        if ((int(temp[0]) >= int(temp[2]) and int(temp[1]) <= int(temp[3])) or ((int(temp[0]) <= int(temp[2]) and int(temp[1]) >= int(temp[3])))):
            count += 1
    print(count)

def calcOverlap2(sections):
    count = 0
    for line in sections:
        line = line.strip()
        temp = re.split(',|-', line)
        if((int(temp[1]) >= int(temp[2]) and int(temp[1]) <= int(temp[3]))):
            count += 1
        elif((int(temp[0]) <= int(temp[3]) and int(temp[1]) >= int(temp[3]))):
            count += 1
    print(count)

parseFile()