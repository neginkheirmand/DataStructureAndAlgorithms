poshte=[]
#O(1)
def pushToPoshte(number):
        poshte.append(number)

#O(1)
def pop():
        if len(poshte)==0:
                return
        poshte.pop()

#O(1)
def printPoshte():
        for i in range(0, len(poshte)):
                print(poshte[len(poshte)-1-i], end=' ')
        print()

#O(1)
def getMiddle():
        if len(poshte)==0:
                return -1
        return int((len(poshte)-1)/2)

#O(1)
def findMiddleOfPoshte():
        middle = getMiddle()
        if middle==-1:
                print(-1)
                return
        print(poshte[middle])
        return

# O(n) : cause the function del works with time complexity of O(n), since after removing the element in the middle all the elements before it (n/2) should be shifted
# dont know of a way to keep a pointer in the middle of the list to delete only that one, like a reverse linked list 
# so i guess the solution is to implement a reverse linked list in python:)
def removeMiddleOfPoshte():
        middle = getMiddle()
        if middle==-1:
                return
        del poshte[middle]
        return

def main():
        inputForm = input().split()
        while inputForm[0]!="finish":
                if inputForm[0]=="push":
                        pushToPoshte(int(inputForm[1]))
                elif inputForm[0]=="pop":
                        pop()
                elif inputForm[0]=="print":
                        printPoshte()
                elif inputForm[0]=="findMiddle":
                        findMiddleOfPoshte()
                elif inputForm[0]=="removeMiddle":
                        removeMiddleOfPoshte()
                inputForm = input().split()

main()