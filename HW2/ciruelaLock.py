def main():
    inputString = input().split()
    numLocks = int(inputString[0]) 
    lockNumbers = int(inputString[1]) 
    # if numLocks==0 or lockNumbers==0:
    locks = []
    positionOfLocks = []
    for i in range(0, numLocks):
        newLock = []
        inputString = input().split()
        for j in range(0, lockNumbers):
            newLock.append(int(inputString[j]))
        positionOfLocks.append(0)
        locks.append(newLock)
    num = input()
    if num!=0:
        redSolution = input().split()
        for i in range(0, len(redSolution)):
            redSolution[i]= int(redSolution[i])
        repeatTimes = int(input())

        for i in range(0, repeatTimes):
            positionOfLocks[i%len(locks)]+=redSolution[i%len(redSolution)]
        for i in range(0, numLocks):
            # and to count the other rotation we just add the repeatTimes  
            positionOfLocks[(i+repeatTimes)%len(positionOfLocks)]= positionOfLocks[(i+repeatTimes)%len(positionOfLocks)]%lockNumbers
            print(locks[(i+repeatTimes)%len(positionOfLocks)][positionOfLocks[(i+repeatTimes)%len(positionOfLocks)]], end='')
main()