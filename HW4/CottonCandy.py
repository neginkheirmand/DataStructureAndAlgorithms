n = 0
edges = []
startNode = 0 
endNode = 0
Length = 0
def getInput():
    n = int(input())
    for i in range(0, n):
        data = input().split()
        edge = (int(data[0]), int(data[1]), int(data[2]))
        edges.append(edge)
    data = input().split()
    startNode = int(data[0])
    endNode = int(data[1])
    Length = int(data[2])
    

def main():
    #get input from user
    getInput()
    

if __name__ == "__main__":
    main()
