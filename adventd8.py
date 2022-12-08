import numpy as np

def parseFile():
    fp = r"C:\Users\E1413175\Desktop\Misc\Python\adventd8.txt"
    file = open(fp, "r")
    temp = file.readlines()
    trees = []
    for i in range(len(temp)):
        trees.append(list(temp[i].strip()))
    trees = np.array(trees)
    trees = trees.astype(int)
    findTrees(trees)
    treesSeen(trees)

def findTrees(trees):

    count = len(trees[0])*2 + (len(trees)-2)*2

    for row in range(1,len(trees)-1):
        for col in range(1, len(trees[row])-1):
            tree = trees[row][col]
            xmax1 = max(trees[row][0:col])
            ymax1 = max(trees[0:row, col])
            xmax2 = max(trees[row][col+1:])
            ymax2 = max(trees[row+1:,col])
            if((tree > xmax1) or (tree > ymax1) or (tree > xmax2) or (tree > ymax2)):
                count += 1
    print(count)

def treesSeen(trees):
    maxScore = 0
    for row in range(1,len(trees)-1):
        for col in range(1, len(trees[row])-1):
            tree = trees[row][col]
            x1, x2, y1, y2 = (0,0,0,0)

            i = row +1
            j = col
            while i <= (len(trees[row])-1):
                if tree > trees[i][j]:
                    y1 += 1
                else:
                    y1 += 1
                    break
                i+=1
            
            i = row -1
            while i >= 0:
                if tree > trees[i][j]:
                    y2 += 1
                else:
                    y2 += 1
                    break
                i-=1

            i = row
            j = col +1
            while j <= (len(trees)-1):
                if tree > trees[i][j]:
                    x1 += 1
                else:
                    x1 += 1
                    break
                j+=1

            j = col -1
            while j >= 0:
                if tree > trees[i][j]:
                    x2 += 1
                else:
                    x2 += 1
                    break
                j-=1
            if((x1*x2*y1*y2) > maxScore):
                maxScore = x1*x2*y1*y2
    print(maxScore)
                
parseFile()