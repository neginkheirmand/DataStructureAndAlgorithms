#the algorithm = A*(a fast graph travesal technique and path-finding algorithm) == dijikstra but improved
#the only problem is: for A* there has to be a start point and only one  final destination, here
#we have more than one destination point since there are more than one ski station spread over the map, solution?
#we find the shortest path from each point of the map to each of the stations and its cost and we compare it to other options, we choose the shortest one

map = []
n=0
m = 0
output=[]

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
