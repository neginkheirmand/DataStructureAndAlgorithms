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
    print(output)



def mapIterate():
    while len(stations)!=0:
        stations[0]

        




def main():
    #get input from user
    getInput()
    mapIterate()

if __name__ == "__main__":
    main()
