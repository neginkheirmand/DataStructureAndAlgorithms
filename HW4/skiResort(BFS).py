# another solution for the ski resort problem this time with BFS algorithm

skiMap = []
n=0
m = 0
output=[]
stations = []


class Node:
    #the node has a depth value, a row number and a column number
    def __init__(self, r, c, depth):
        self.r = r
        self.c = c
        self.depth = depth



def getInput():
    global n , m
    global skiMap
    global stations
    data=input().split()
    n = int(data[0])
    m = int(data[1])
    mapRow = []
    outputRow = []
    for i in range(0, n):
        data = input()
        for j in range(0, m):
            mapRow.append(data[j])
            outputRow.append(-1)
            if data[j]=='M':
                stations.append(Node(i, j, 0))
        skiMap.append(mapRow)
        output.append(outputRow)
        mapRow=[]
        outputRow=[]


def addNeighbours(node, stationList):
    r = node.r
    c = node.c
    depth = node.depth
    global skiMap
    global output
    global n, m
    #upper neighbour
    if r-1>=0 and skiMap[r-1][c]!='X' and ( output[r-1][c]==-1 or output[r-1][c]>depth+1):
        stationList.append(Node(r-1, c, depth+1))
    #buttom
    if r+1<n and skiMap[r+1][c]!='X' and ( output[r+1][c]==-1 or output[r+1][c]>depth+1):
        stationList.append(Node(r+1, c, depth+1))
    #left
    if c-1>=0 and skiMap[r][c-1]!='X' and ( output[r][c-1]==-1 or output[r][c-1]>depth+1):
        stationList.append(Node(r, c-1, depth+1))
    #ritgh
    if c+1<m and skiMap[r][c+1]!='X' and ( output[r][c+1]==-1 or output[r][c+1]>depth+1):
        stationList.append(Node(r, c+1, depth+1))

    


def mapIterate():
    global stations
    while len(stations)!=0:
        node = stations.pop(0)
        if output[node.r][node.c]> int(node.depth) or output[node.r][node.c]==-1: 
            output[node.r][node.c]=int(node.depth)
        addNeighbours(node, stations)

def printOutput():
    global output
    global n, m
    for i in range(0, n):
        for j in range(0, m):
            print( output[i][j], end=' ')
        print()


def main():
    #get input from user
    getInput()
    mapIterate()
    printOutput()
    # print("\033[1;31m")
    # print(output)
    # print("\033[0;0m")

if __name__ == "__main__":
    main()
