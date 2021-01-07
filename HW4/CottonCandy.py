n = 0
edges = []
startNode = 0 
endNode = 0
Length = 0
Nodes = []  # a list of all nodes and their respective neighbours

def existsInList(nodes, node):
    for i in range(0, len(nodes)):
        if nodes[i]==node:
            return True
        return False

def getInput():
    n = int(input())
    for i in range(0, n):
        data = input().split()
        #edge
        edge = (int(data[0]), int(data[1]), int(data[2]))
        edges.append(edge)
        #node
        if not existsInList(Nodes, int(data[0])):
            Nodes.append( [int(data[0]) , int(data[1])] )
        if not existsInList(Nodes, int(data[1])):
            Nodes.append(data[1])
    data = input().split()
    startNode = int(data[0])
    endNode = int(data[1])
    Length = int(data[2])
    

def main():
    #get input from user
    getInput()
    

if __name__ == "__main__":
    main()
