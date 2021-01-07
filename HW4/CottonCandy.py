#will Use Bellman-Ford algorithm for this question since dijikstra does'nt support negative edges 
numEdges = 0
edges = []
startNode = 0 
endNode = 0
Length = 0
numVert = 0
Nodes = []  # a list of all nodes 

def existsInList(nodes, node):
    for i in range(0, len(nodes)):
        if nodes[i]==node:
            return True
        return False

def getInput():
    global numEdges, startNode, endNode, Length, edges
    numEdges = int(input())
    for i in range(0, numEdges):
        data = input().split()
        #edge
        edge = (int(data[0]), int(data[1]), int(data[2]))
        #edges list contains tuples of (start, end, weigth)
        edges.append(edge)
        #node
        if not existsInList(Nodes, int(data[0])):
            Nodes.append( int(data[0]) )
        if not existsInList(Nodes, int(data[1])):
            Nodes.append( int(data[1]) )
    data = input().split()
    startNode = int(data[0])
    endNode = int(data[1])
    Length = int(data[2])

def getIndex(value, listNodes):
    for i in range(0, len(listNodes)):
        if listNodes[i]==value:
            return i
    

def runBFalgorithm():
    global numEdges, numVert
    #we know there can be atmost |v|-1 edges in a path from s to e since we can |v| vertices, so we repeat the procedure above |v|-1 times and stop only if nothing 
    #was updated before |v|-1 repetition times is completed
    numRepetition = numVert-1
    global Nodes
    # we create the list with nodes  and costs of them  (starting with infinity- 99999 should be enough -)
    costPath = []
    for i in range(0, numVert):
        costPath.append([Nodes[i], 99999] )
    
    global startNode
    indexStartNode = getIndex(startNode, costPath)
    costPath[indexStartNode]=0
    stopFlag = False
    for i in range(0, numRepetition):
        stopFlag = False
        #here we loop over the nodes and change their costs (if possible) and if no values where changed we break the loop
        for j in range(0, numVert):
            


     


def main():
    #get input from user
    getInput()

    

if __name__ == "__main__":
    main()
