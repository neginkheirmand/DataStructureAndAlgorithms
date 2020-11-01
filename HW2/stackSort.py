def main():
        inputForm = input().split()
        stack = []
        for i in range(0,len(inputForm)):
                stack.append(int(inputForm[len(inputForm)-1-i]))
        #standard stack ready. Im just worried about the extra time taken -because i'm using list as a stack- for memory allocation.
        secondaryStack = []
        tempFirst = 1  
        tempSec = None
        while True:
                if len(stack)==0:
                        break
                temp = stack.pop()
                if temp == tempFirst:
                        tempFirst+=1
                        while tempSec==tempFirst:
                                secondaryStack.pop()
                                if len(secondaryStack)!=0:
                                        tempSec = secondaryStack[len(secondaryStack)-1]
                                else:
                                        tempSec=None
                                tempFirst+=1
                        continue
                if tempSec == None:
                        tempSec = temp
                        secondaryStack.append(temp)
                        continue
                if tempSec<temp:
                        print("no")
                        return
                tempSec=temp
                secondaryStack.append(temp)
        print("yes")
main()