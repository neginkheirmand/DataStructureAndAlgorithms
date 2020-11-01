inputForm = input().split()
stack = []
for i in range(0,len(inputForm)):
        stack.append(int(inputForm[len(inputForm)-1-i]))
#standard stack ready. Im just worried about the extra time taken -because i'm using list as a stack- for memory allocation.
 