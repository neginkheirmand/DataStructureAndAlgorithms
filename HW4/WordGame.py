alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=0
m=0
chart = []
startLetter = "0"
paths=[]

class Path:
    def __init__(self, length, r, c):
        self.length = length 
        self.r=r
        self.c=c

def getInput():
    global n, m, chart
    global startLetter
    data = input().split()
    n = int(data[0])
    m = int(data[1])

    for i in range(0, n):
        data = input().split()
        chart.append(data)
    startLetter = input()  

def findStartLetter():
    global startLetter
    global n, m
    for i in range(0, n):
        for j in range(0, m):
            if chart[i][j]==startLetter:
                paths.append(Path(1, i, j))

def FindWord(length, r, c, indexFinal):
    global chart
    global alphabet
    global n, m
    global paths
    global startLetter
    
    if chart[r][c]!=alphabet[(alphabet.index(startLetter)+length-1)%len(alphabet)]:
        return False

    output = False
    #straight moves
    #Upper neighbour
    if r-1>=0:
        if FindWord(length+1, r-1, c, indexFinal):
            output = True
    #bottom neighbour
    if r+1<n:
        if FindWord(length+1, r+1, c, indexFinal):
            output = True
    #left neighbour
    if c-1>=0:
        if FindWord(length+1, r, c-1, indexFinal):
            output = True
    #right neighbour
    if c+1<m:
        if FindWord(length+1, r, c+1, indexFinal):
            output = True
    
    #diagonal moves
    #Upper-left neighbour
    if r-1>=0 and c-1>=0:
        if FindWord(length+1, r-1, c-1, indexFinal):
            output = True
    #bottom-right neighbour
    if r+1<n and c+1<m:
        if FindWord(length+1, r+1, c+1, indexFinal):
            output = True
    #buttom-left neighbour
    if r+1<n and c-1>=0:
        if FindWord(length+1, r+1, c-1, indexFinal):
            output = True
    #Upper-right neighbour
    if r-1>=0 and c+1<m:
        if FindWord(length+1, r-1, c+1, indexFinal):
            output = True

    if output:
        return True
    #if came to here, means non of the neighbours is the next letter, meaning the length of the path is the length -1
    if paths[indexFinal].length < length :
        paths[indexFinal].length = length
    return False

def findBestPath():
    global paths
    maximum =1
    index = -1
    for i in range(0, len(paths)):
        FindWord(1, paths[i].r, paths[i].c, i)
        if maximum < paths[i].length:
            maximum = paths[i].length
            index = i
    return index

def printOutput(i):
    global paths
    print(paths[i].length)
    print(paths[i].r, paths[i].c)

def main():
    #get input from user
    getInput()
    findStartLetter()
    indexChosen = findBestPath()
    printOutput(indexChosen)

    

if __name__ == "__main__":
    main()
