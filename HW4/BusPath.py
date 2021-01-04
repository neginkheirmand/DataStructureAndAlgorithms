
paths = []
n = 0
visited = []
finalpath=[]

class Path:
    def __init__(self, startStation, destination):
        self.start = startStation
        self.dest = destination

def getInput():
    global paths
    global n
    global visited
    n = int(input())
    data = input().split()
    visited.append(False)
    for i in range(0, n-1):
        visited.append(False)
        paths.append( Path( int(data[i]), i+2 ))

def getNeighbours(indexNode):
    global paths
    neighbours = []
    for i in range(0, len(paths)):
        if paths[i].start == (indexNode+1):
            neighbours.append(paths[i].dest)
    return neighbours

def dfs(indexNode):
    global visited
    global finalpath
    global n

    if visited[indexNode]:
        return False

    visited[indexNode]=True

    if indexNode == n-1:
        #then its the last node
        finalpath.append(indexNode+1)
        return True
    neighbours=getNeighbours(indexNode)
    for i in range(0, len(neighbours)):
        found = dfs(neighbours[i]-1)
        if found:
            finalpath.append(indexNode+1)
            return True
    return False

def mapIterate():
    dfs(0)

def printOutput():
    global finalpath
    for i in range(0, len(finalpath)):
        print(finalpath[len(finalpath)-1-i], end=' ')
    
def main():
    #get input from user
    getInput()
    #the function that will call dfs(0), it was not necesary, just for sake of clean code
    mapIterate()
    #print the output in reverse order of the list, because was added in the backtracking functions, going from the leaves of the tree to the root
    printOutput()

if __name__ == "__main__":
    main()