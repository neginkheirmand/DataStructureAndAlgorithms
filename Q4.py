def main():
    numElements = int(input("please enter the number of elements in the list\n"))
    while numElements<=0:
        numElements = int(input("please enter the number of elements in the list\n"))
    listOfElements = input("enter the elements of the list in the next row\n").split()
    for i in range(0, numElements):
        listOfElements[i] = int(listOfElements[i])

    print("this scrypt should find numbers a and b in the list specified that can satisfy the condition: a+b = k")
    #finding 
    k = int(input("please enter k: "))

    for i in range(0, numElements):
        for j in range(i+1, numElements):
            if listOfElements[i]+listOfElements[j]==k :
                print("list[{}] = {}\nlist[{}] = {}\n{}+{}={}".format(i,listOfElements[i],j, listOfElements[j], listOfElements[i], listOfElements[j], k))
                return
