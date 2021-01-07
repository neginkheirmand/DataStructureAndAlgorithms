n = 0
def main():
    global n
    n = input()
    n = int(n)
    for i in range(0, n):
        #the (x, y) tuple
        tupleState = (0,0)
        #the neighbours list, [N, E, S, W)]
        #if the value in the first house of list is 1 means the path from the house in the north of this house (x, y) has been used once
        neighbours = [0,0,0,0]
        data = input()
        movesDic = {}
        movesDic[tupleState] = neighbours
        for j in range(0, len(data)):
            if data[j]=='N':
                #we find the house and plus 1 to the north neighbour
                edgesRepetition = movesDic[tupleState]
                edgesRepetition[0]=edgesRepetition[0]+1
                movesDic[tupleState]= edgesRepetition
                #now to the new house
                newtupleState=(tupleState[0], tupleState[1]+1)
                tupleState = newtupleState
                #it either already exists in the dictionary or we add it 
                if newtupleState in movesDic:
                    edgesRepetition = movesDic[newtupleState]
                    edgesRepetition[2]=edgesRepetition[2]+1
                    movesDic[newtupleState] = edgesRepetition
                else:
                    #add the new house to the dic
                    movesDic[newtupleState]= [0,0,1,0]
            elif data[j]=='S':
                #we find the house and plus 1 to the south neighbour
                edgesRepetition = movesDic[tupleState]
                edgesRepetition[2]=edgesRepetition[2]+1
                movesDic[tupleState]= edgesRepetition
                #now to the new house
                newtupleState=(tupleState[0], tupleState[1]-1)
                tupleState = newtupleState
                #it either already exists in the dictionary or we add it 
                if newtupleState in movesDic:
                    edgesRepetition = movesDic[newtupleState]
                    edgesRepetition[0]=edgesRepetition[0]+1
                    movesDic[newtupleState] = edgesRepetition
                else:
                    #add the new house to the dic
                    movesDic[newtupleState]= [1,0,0,0]
            elif data[j]=='E':
                #we find the house and plus 1 to the east neighbour
                edgesRepetition = movesDic[tupleState]
                edgesRepetition[1]=edgesRepetition[1]+1
                movesDic[tupleState]= edgesRepetition
                #now to the new house
                newtupleState=(tupleState[0]+1, tupleState[1])
                tupleState = newtupleState
                #it either already exists in the dictionary or we add it 
                if newtupleState in movesDic:
                    edgesRepetition = movesDic[newtupleState]
                    edgesRepetition[3]=edgesRepetition[3]+1
                    movesDic[newtupleState] = edgesRepetition
                else:
                    #add the new house to the dic
                    movesDic[newtupleState]= [0,0,0,1]
            elif data[j]=='W':
                #we find the house and plus 1 to the west neighbour
                edgesRepetition = movesDic[tupleState]
                edgesRepetition[3]=edgesRepetition[3]+1
                movesDic[tupleState]= edgesRepetition
                #now to the new house
                newtupleState=(tupleState[0]-1, tupleState[1])
                tupleState = newtupleState
                #it either already exists in the dictionary or we add it 
                if newtupleState in movesDic:
                    edgesRepetition = movesDic[newtupleState]
                    edgesRepetition[1]=edgesRepetition[1]+1
                    movesDic[newtupleState] = edgesRepetition
                else:
                    #add the new house to the dic
                    movesDic[newtupleState]= [0,1,0,0]
        #now the movesDic stores the edges of the graph
        #we have to the number of one time passed edges and other more repeated edged, just have in acount each edges is counted two times, since we store the
        #nodes instead of the actual edges
        oneRepetition = 0
        moreThanOne = 0
        newEdge = 0
        for key in movesDic:
            listMove = movesDic[key]
            for k in range(0, len(listMove)):
                if listMove[k] == 1:
                    oneRepetition+=1
                elif listMove[k] != 1 and listMove[k] != 0:
                    moreThanOne+=listMove[k]
                    newEdge+=1
        answer = newEdge*4
        answer+=moreThanOne
        answer+=oneRepetition*5
        print(int(answer/2))




if __name__ == "__main__":
    main()
