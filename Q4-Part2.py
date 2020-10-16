def positionFinder(eList, num, start, end):
    print(eList[start:end+1])
    if end-start==1:
        if eList[start] == num:
            return start
        elif eList[end] == num:
            return end
        else:
            return -1
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
    numElements = int(input("please enter the number of elements in the list\n"))
    while numElements<=0:
        numElements = int(input("please enter the number of elements in the list\n"))
    listOfElements = input("enter the elements of the list in the next row(should be sorted from min to max)\n").split()
    for i in range(0, numElements):
        listOfElements[i] = int(listOfElements[i])

    print("this scrypt should find numbers a and b in the sorted list specified that can satisfy the condition: a+b = k")
    k = int(input("please enter k: "))

    print(positionFinder(listOfElements, k, 0, len(listOfElements)-1 ) )
    #find position of k/2
    # for i in range(0, numElements):
    #     for j in range(i+1, numElements):
    #         if listOfElements[i]+listOfElements[j]==k :
    #             print("list[{}] = {}\nlist[{}] = {}\n{}+{}={}".format(i,listOfElements[i],j, listOfElements[j], listOfElements[i], listOfElements[j], k))
    #             return
    # print("none of the elements in the list, can satisfy the condition specified")
main()