def main():
    inputString = input().split()
    numLocks = int(inputString[0]) 
    lockNumbers = int(inputString[1]) 
    locks = []
    positionOfLocks = []
    for i in range(0, numLocks):
        newLock = []
        inputString = input().split()
        for j in range(0, lockNumbers):
            newLock.append(int(inputString[j]))
        positionOfLocks.append(0)
        locks.append(newLock)
    input()
    redSolution = input().split()
    for i in range(0, len(redSolution)):
        redSolution[i]= int(redSolution[i])
    repeatTimes = int(input())

    for i in range(0, repeatTimes):
        positionOfLocks[i%len(locks)]+=redSolution[i%len(redSolution)]
    for i in range(0, numLocks):
        positionOfLocks[i]= positionOfLocks[i]%lockNumbers
        print(locks[i][positionOfLocks[i]], end='')
main()
# print(-1%5)