#the algorithm = A*(a fast graph travesal technique and path-finding algorithm) == dijikstra but improved
#the only problem is: for A* there has to be a start point and only one  final destination, here
#we have more than one destination point since there are more than one ski station spread over the map, solution?
#we find the shortest path from each point of the map to each of the stations and its cost and we compare it to other options, we choose the shortest one

map = []
n=0
m = 0
output=[]

class Node:
    def __init__(self, r, c, rDestination, cDestination, g):
        self.r = r
        self.c = c
        self.h = self.getHvalue(rDestination, cDestination, r, c)
        self.g = g

    def updateGValue(self, newg):
        if self.g > newg:
            self.g = newg

    def getHvalue(self, rDestination, cDestination, r, c):
        #the H value:  the estimated movement cost to move from that given square on the grid to the final destination.
        #we can use the Pythagoras theorem to get the distance but i prefer this method 
        return abs(rDestination-r)+abs(cDestination-c)

    def getFvalue( self ):
        return self.g + self.h

def containsNode(r, c, openedlist, newg):
    #this method's function is to tell if a node with passed r and c exists in the list, if so update its Gvalue(if necessary) 
    #return true if exists and False if not
    for i in range(0, len(openedlist)):
        if Node(openedlist[i]).c == c and Node(openedlist[i]).r == r:
            #the G value will be updated (if necessary)
            Node(openedlist[i]).updateGValue(newg) 
            return True
    return False

def getGvalue():
    #the G value:  the movement cost to move from the starting point to a given square on the grid, following the path generated to get there.
    print("Gvalue")


def addNeighbours(openList, r, c, nodeG, rDestination, cDestination):
#this method's function is to find the neighbours of the node in r, c and add them to the openList if they are not already in there
# and update their g value in case we have find a shorter path to them 

    #upper neighbour( if existent and available and non-repetitive)
    if r-1>=0 and map[r-1][c]!='X'and not containsNode(r-1, c, openList, nodeG+1):
            openList.append(Node(r-1, c, rDestination, cDestination, nodeG+1))

    #bottom neighbour( if existent and available and non-repetitive)
    if r+1<n and map[r+1][c]!='x' and not containsNode(r+1, c, openList, nodeG+1):
            openList.append(Node(r+1, c, rDestination, cDestination, nodeG+1))
    
    #left neighbour( if existent and available and non-repetitive)
    if c-1>=0 and map[r][c-1]!='X' and not containsNode(r, c-1, openList, nodeG+1):
        openList.append(Node(r, c-1, rDestination, cDestination, nodeG+1))

    #right neighbour( if existent and available and non-repetitive)
    if c+1<m and map[r][c+1]!='X' and not containsNode(r, c+1, openList, nodeG+1):
        openList.append(Node(r, c+1, rDestination, cDestination, nodeG+1))

def findBestNode(openList):
    #this methods find the best candidate to next move and returns its index in the open list
    min=Node(openList[0]).getFvalue()
    hValue = Node(openList[0]).getHvalue()
    index = 0
    for i in range(1, len(openList)):
        if min > Node(open[i]).getFvalue():
            min = Node(open[i]).getFvalue()
            hValue = Node(openList[i]).getHvalue()
            index = i
        elif min == Node(open[i]).getFvalue() and hValue > Node(open[i]).getHvalue :
            hValue = Node(openList[i]).getHvalue()
            index = i
    return i

def shortestPath(rStart, cStart, r2, c2):
    #this method finds the shortest path between point in row r1 and column c1 of the map and point in row r2 and column c2
    #and returns the distance of the shortest path available
    #we dont need to keep the parent of each node, just update the distances if needed
    openList = []
    closedList = []
    startNode = Node(rStart, cStart, r2, c2)
    openList.append(startNode)
    while len(open)!=0:
        indexBest = findBestNode(openList)
        openList.pop(indexBest)


     

def mapIterator():
    print("iterate")
    

def getInput():
    data=input().split()
    n = int(data[0])
    m = int(data[1])
    mapRow = []
    for i in range(0, n):
        data = input()
        for j in range(0, m):
            mapRow.append(data[j])
        map.append(mapRow)
        mapRow=[]
    print(map)


def main():
    getInput()


if __name__ == "__main__":
    main()
