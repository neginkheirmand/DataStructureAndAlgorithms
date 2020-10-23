def positionFinder(eList, num, start, end):
    # print(eList[start:end+1])
    if end-start==1:
        if eList[start] == num:
            return start
        elif eList[end] == num:
            return end
        else:
            return None
    if (start+end)%2==1:
        if num>=eList[ 1 + int( (start+end)/2 ) ]:
            return positionFinder(eList, num, 1 + int( (start+end)/2 ), end)
        else:
            return positionFinder(eList, num, start, 1 + int( (start+end)/2 ))
    else:
        if num>=eList[ int( (start+end)/2 ) ]:
            return positionFinder(eList, num, int( (start+end)/2 ), end)
        else:
            return positionFinder(eList, num, start, int( (start+end)/2 ))


def main():
    numElements = int(input("size of the list?\n"))
    while numElements<=0:
        numElements = int(input("size of the list?\n"))
    listOfElements = input("list entries(should be sorted from min to max)\n").split()
    for i in range(0, numElements):
        listOfElements[i] = int(listOfElements[i])

    print("find a and b in the sorted list that can satisfy the condition: a+b = k")
    k = int(input("please enter k: "))
    for i in range(0, len(listOfElements) - 1 ):
        print(listOfElements[i])
        b = k - listOfElements[i]
        positionFound = positionFinder(listOfElements, b, 0, len(listOfElements)-1)
        # print('\033[93m', positionFound, '\033[0m')
        if positionFound!=None:
            print("this list satisfies the condition")
            print("{} + {} = {}".format(listOfElements[i], b, k))
            return
    print("this list does not satisfy the condition")
main()