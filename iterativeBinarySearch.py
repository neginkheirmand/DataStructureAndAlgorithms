def main():
    n = int(input("size of the list?\n"))
    while n<=0:
        n = int(input("size of the list?\n"))
    eList = input("list entries(should be sorted from min to max)\n").split()
    for i in range(0, n):
        eList[i] = int(eList[i])

    print("find a and b in the sorted list that can satisfy the condition: a+b = k")
    k = int(input("please enter k: "))
    for i in range(0, n-1 ):
        # print(eList[i])
        b = k - eList[i]    
        ##have the b, now we see if it exists in the array
        index = None
        start = 0
        end = n-1
        mid = int((n-1)/2)
        while mid<=end:
            # print(eList[start: end+1])
            # print(start, end)
            if end-start<=1:
                if eList[start]==b:
                    index = start
                elif eList[end] == b:
                    index = end
                break                
            mid = int((end+start)/2)
            if eList[mid]>b:
                end = mid
            else:
                start = mid
        # print('\033[93m', positionFound, '\033[0m')
        if index!=None:
            print("this list satisfies the condition")
            print("{} + {} = {}".format(eList[i], b, k))
            return
    print("this list does not satisfy the condition")
    
    
    
main()