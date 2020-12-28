#the algorithm = A*(a fast graph travesal technique and path-finding algorithm) == dijikstra but improved
#the only problem is: for A* there has to be a start point and only one  final destination, here
#we have more than one destination point since there are more than one ski station spread over the map, solution?
#we find the shortest path from each point of the map to each of the stations and its cost and we compare it to other options, we choose the shortest one

skiMap = []
n=0
m = 0
output=[]
stations = []
class Node:
    #the node has h value and g value and f = g + h
    #the G value:  the movement cost to move from the starting point to a given square on the grid, following the path generated to get there.
    #the H value:  the estimated movement cost to move from that given square on the grid to the final destination.

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
        if openedlist[i].c == c and openedlist[i].r == r:
            #the G value will be updated (if necessary)
            openedlist[i].updateGValue(newg) 
            return True
    return False


def addNeighbours(openList, parentNode, rDestination, cDestination, closedList):
#this method's function is to find the neighbours of the node in r, c and add them to the openList if they are not already in there
# and update their g value in case we have find a shorter path to them 

    r = parentNode.r
    c = parentNode.c
    nodeG = parentNode.g
    global n, m
    global skiMap

    #upper neighbour( if existent and available and non-repetitive)
    if r-1>=0 and skiMap[r-1][c]!='X'and not containsNode(r-1, c, openList, nodeG+1) and not containsNode(r-1, c, closedList, nodeG+1):
        openList.append(Node(r-1, c, rDestination, cDestination, nodeG+1))
        if r-1 ==rDestination and c == cDestination:
            return True


    #bottom neighbour( if existent and available and non-repetitive)
    if r+1<n and skiMap[r+1][c]!='X' and not containsNode(r+1, c, openList, nodeG+1) and not containsNode(r+1, c, closedList, nodeG+1):
        openList.append(Node(r+1, c, rDestination, cDestination, nodeG+1))
        if r+1 == rDestination and c == cDestination:
            return True

    #left neighbour( if existent and available and non-repetitive)
    if c-1>=0 and skiMap[r][c-1]!='X' and not containsNode(r, c-1, openList, nodeG+1) and not containsNode(r, c-1, closedList, nodeG+1):
        openList.append(Node(r, c-1, rDestination, cDestination, nodeG+1))
        if r == rDestination and c-1 == cDestination:
            return True

    #right neighbour( if existent and available and non-repetitive)
    if c+1<m and skiMap[r][c+1]!='X' and not containsNode(r, c+1, openList, nodeG+1) and not containsNode(r, c+1, closedList, nodeG+1):
        openList.append(Node(r, c+1, rDestination, cDestination, nodeG+1))
        if r == rDestination and c+1 == cDestination:
            return True
    return False

def findBestNode(openList):
    #this methods find the best candidate to next move and returns its index in the open list
    min=openList[0].getFvalue()
    hValue = openList[0].h
    index = 0
    for i in range(1, len(openList)):
        if min > openList[i].getFvalue():
            min = openList[i].getFvalue()
            hValue = openList[i].h
            index = i
        elif min == openList[i].getFvalue() and hValue > openList[i].h :
            hValue = openList[i].h
            index = i
    return index
    

def shortestPath(rStart, cStart, r2, c2):
    #this method finds the shortest path between point in row r1 and column c1 of the map and point in row r2 and column c2
    #and returns the distance of the shortest path available
    #we dont need to keep the parent of each node, just update the distances if needed
    openList = []
    closedList = []
    startNode = Node(rStart, cStart, r2, c2, 0)
    openList.append(startNode)
    while len(openList)!=0:
        # print("openlist:")
        # for x in range(len(openList)): 
        #     print (openList[x].r, openList[x].c, openList[x].g, openList[x].h)
        
        # print("closedlist:")
        # for x in range(len(closedList)): 
        #     print (closedList[x].r, closedList[x].c, closedList[x].g, closedList[x].h)

        indexBest = findBestNode(openList)
        # print(indexBest)
        done = addNeighbours(openList, openList[indexBest], r2, c2 , closedList)
        if done:
            #we have find the shortest path, now we have to return its length
            #the last element of the list is the destination node 
            #the length of the way is the g cost of the last node
            return openList[len(openList)-1].g
        closedList.append(openList.pop(indexBest))
        # print("openlist:")
        # for x in range(len(openList)): 
        #     print (openList[x].r, openList[x].c, openList[x].g, openList[x].h)
        
        # print("closedlist:")
        # for x in range(len(closedList)): 
        #     print (closedList[x].r, closedList[x].c, closedList[x].g, closedList[x].h)
        # print()
        # print()
        # print()

    return -5

def mapIterator():

    global n, m
    global skiMap
    global stations
    for i in range(0, n):
        for j in range(0, m):
            if skiMap[i][j]=='X':
                print( "-1", end=' ')
            elif skiMap[i][j]=='M':
                print( "0", end=' ')
            else:
                #go find the path cost here and all the stations, the shortest one is the number in this house of output
                minPath = shortestPath(i, j, stations[0][0], stations[0][1])
                for s in range(1, len(stations)):
                    temp = shortestPath(i, j, stations[s][0], stations[s][1])
                    if temp<minPath:
                        minPath= temp
    
                print( minPath, end=' ')
        print()
                


    

def getInput():
    global n , m
    global skiMap
    global stations
    data=input().split()
    n = int(data[0])
    m = int(data[1])
    mapRow = []
    for i in range(0, n):
        data = input()
        for j in range(0, m):
            mapRow.append(data[j])
            if data[j]=='M':
                stations.append([i, j])
        skiMap.append(mapRow)
        mapRow=[]
    # print(stations)



def main():
    getInput()
    mapIterator()


if __name__ == "__main__":
    main()
