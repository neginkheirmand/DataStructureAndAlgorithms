poshte=[]
def pushToPoshte(number):
        poshte.append(number)

def pop():
        if len(poshte)==0:
                return
        poshte.pop()

def printPoshte():
        for i in range(0, len(poshte)):
                print(poshte[len(poshte)-1-i], end=' ')
        print()

def getMiddle():
        if len(poshte)==0:
                return -1
        return int((len(poshte)-1)/2)

def findMiddleOfPoshte():
        middle = getMiddle()
        if middle==-1:
                print(-1)
                return
        print(poshte[middle])
        return

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