def parseFile():
    fp = r"C:\Users\E1413175\Desktop\Misc\Python\adventd2.txt"
    file = open(fp, "r")
    games = file.readlines()
    #calcScores2(games)
    calcScores2(games)

def calcScores1(games):
    scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    sum = 0
    for i in games:
        i = i.strip()
        sum += scores[i]
    print(sum)

def calcScores2(games):
    scores = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    sum = 0
    for i in games:
        i = i.strip()
        sum += scores[i]
    print(sum)

parseFile()
