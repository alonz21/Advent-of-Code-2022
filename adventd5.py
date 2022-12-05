def parseFile():
    fp = r"C:\Users\E1413175\Desktop\Misc\Python\adventd5.txt"
    file = open(fp, "r")
    crates = []
    for line in file:
        line = line.rstrip()
        crates.append(line)
    makeStacks(crates)

def makeStacks(crates):
    stacks = [[] for i in range(2)]
    for line in crates:
        offset = 0
        count = 0
        for i in range(len(line)):
            chr = line[i]
            if chr == '1':
                #moveCrates(stacks, crates)
                moveCrates2(stacks, crates)
                return
            if chr != '[' and chr != ']':
                if chr == ' ':
                    count += 1
                    if count == 4:
                        offset += 1
                        if len(stacks) <= offset:
                            stacks.append([])
                        count = 0
                else:
                    if len(stacks) <= offset:
                        stacks.append([])
                    stacks[offset].insert(0, chr)
                    offset += 1
                    count = 0

def moveCrates(stacks, moves):
    flg = 0
    for line in moves:
        if line == '':
            flg = 1
            continue
        if flg:
                line = line.split(' ')
                num = int(line[1])
                src = int(line[3])
                dest = int(line[5])

                for i in range(num):
                    stacks[dest-1].append(stacks[src-1].pop())

    print(stacks)

def moveCrates2(stacks,moves):
    flg = 0
    for line in moves:
        if line == '':
            flg = 1
            continue
        if flg:
                line = line.split(' ')
                num = int(line[1])
                src = int(line[3]) - 1
                dest = int(line[5]) - 1

                for i in reversed(range(num)):
                    stacks[dest].append(stacks[src].pop(((i+1)*-1)))

    print(stacks)

parseFile()