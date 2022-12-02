import numpy as np

def parseCals():
    fp = r"C:\Users\E1413175\Desktop\Misc\Python\adventd1.txt"
    file = open(fp, "r")
    cals = file.readlines()
    maxes = [0,0,0]
    sum1 = 0
    for i in cals:
        if i.strip() == "":
            if maxes[0] <= sum1:
                maxes[2] = maxes[1]
                maxes[1] = maxes[0]
                maxes[0] = sum1
            elif maxes[1] <= sum1:
                maxes[2] = maxes[1]
                maxes[1] = sum1
            elif maxes[0] <= sum1:
                maxes[0] = sum1
            sum1 = 0
        else:
            sum1 += int(i)
    print(maxes)
    print(sum(maxes))
    return maxes


parseCals()