#will Use Bellman-Ford algorithm for this question since dijikstra does'nt support negative edges 
numEdges = 0
startNode = 0 
endNode = 0
Length = 0
dictionaryOfNodes={}

finalPath = []

def existsInList(nodes, node):
    for i in range(0, len(nodes)):
        if nodes[i]==node:
            return True
        return False

def getInput():
    global numEdges, startNode, endNode, Length
    global dictionaryOfNodes
    numEdges = int(input())
    for i in range(0, numEdges):
        data = input().split()
        node = int(data[0])
        neighbour =[int(data[1]), int(data[2])] 
        #for the node with outgoing edge
        if node in dictionaryOfNodes:
            neighbours = dictionaryOfNodes[node]
            neighbours.append(neighbour)
            dictionaryOfNodes[node]= neighbours
        else:
            dictionaryOfNodes[node] = []
            dictionaryOfNodes[node].append(neighbour)
        #also for the neighbors
        node = int(data[1])
        if not node in dictionaryOfNodes:
            dictionaryOfNodes[node] = []
    data = input().split()
    startNode = int(data[0])
    endNode = int(data[1])
    Length = int(data[2])

def getCost(array, value):
    for i in range(0, len(array)):
        if array[i][0]==value:
            return array[i][1]

def getPathCost(path):
    global dictionaryOfNodes
    totalCost = 0
    for i in range(1, len(path)):
        neighboursOfNode = dictionaryOfNodes[path[i-1]]
        totalCost+=getCost(neighboursOfNode, path[i] )
    return totalCost

def printOutput(exactPath, costPath):
    global Length
    if len(exactPath)==Length+1:
        for i in range(0, len(exactPath)):
            print(exactPath[i], end = ' ')
        print(costPath)
        return
    global finalPath
    if len(finalPath)!=0:
        for i in range(0, len(finalPath)):
            print(finalPath[i], end = ' ')
        print(getPathCost(finalPath))
        return
    else:
        print("Impossible")



def runBFalgorithm():
    global numEdges, dictionaryOfNodes
    #we know there can be atmost |v|-1 edges in a path from s to e since we can |v| vertices, so we repeat the procedure above |v|-1 times and stop only if nothing 
    #was updated before |v|-1 repetition times is completed
    numRepetition = len(dictionaryOfNodes)-1
    # we create the dictionary with nodes and costs of them  (starting with infinity- 99999 should be enough -)
    costPath = {}
    for key in dictionaryOfNodes:
        costPath[key]= 99999
    #now to save the exact path
    exactPath = {}
    for key in dictionaryOfNodes:
        exactPath[key] = [] 
    #but the cost of the start node must be 0
    global startNode
    global endNode
    global Length
    global finalPaths
    costPath[startNode]=0
    exactPath[startNode]= [startNode]

    stopFlag = False
    for i in range(0, numRepetition):
        stopFlag = True
        #here we loop over the nodes and change their costs (if possible) and if no values where changed we break the loop using stopFlag
        for key in costPath:
            #first we make sure the node is accessible 
            if costPath[key]!=99999:    
                #now we iterate over its neighbours and update their cost if needed
                #so we need the neighbours of this node (the ones connected to this node by outgoing edges of the current node)
                neighbours = dictionaryOfNodes[key]
                #neighbours is a list of all the neighbors of this current node and the cost of the edge to that secundary node [   [neighbour1, cost1], [neighbour2, cost2] , ...   ]
                for j in range(0, len(neighbours)):
                    neighbour = neighbours[j][0]
                    cost = neighbours[j][1]
                    if cost + costPath[key] < costPath[neighbour]:
                        costPath[neighbour]=cost + costPath[key]
                        stopFlag = False
                        #but we also update the exact path 
                        listPathNode = exactPath[key].copy()
                        listPathNode.append(neighbour)
                        exactPath[neighbour] = listPathNode
                        if neighbour == endNode:
                            if len(exactPath[key]) == Length:
                                finalPath=exactPath[neighbour]
        if stopFlag:
            break
    printOutput(exactPath[endNode], costPath[endNode])
    return 
             




     


def main():
    #get input from user
    getInput()
    runBFalgorithm()

if __name__ == "__main__":
    main()
