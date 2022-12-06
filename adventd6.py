def parseFile():
    fp = r".\adventd6.txt"
    file = open(fp, "r")
    packet = file.readlines()
    findMarker(packet)
    findMessage(packet)

def findMarker(packet):
    subPacket = []
    for i in packet[0]:
        subPacket.append(i)
        if len(subPacket) >= 4:
            marker = subPacket[-4::1]
            if(len(set(marker)) == len(marker)):
                print(len(subPacket))
                return(len(subPacket))

def findMessage(packet):
    subPacket = []
    for i in packet[0]:
        subPacket.append(i)
        if len(subPacket) >= 14:
            marker = subPacket[-14::1]
            if(len(set(marker)) == len(marker)):
                print(len(subPacket))
                return(len(subPacket))

parseFile()