#if Ur asking about the file name : i just wanted to make it look fun
inputString = input().split()
cargo = []
for i in range(0, len(inputString)):
        cargo.append(int(inputString[i]))
cargo.insert(0, cargo.pop())
insertionIndex = 2
while insertionIndex<len(cargo)-1:
        cargo.insert(insertionIndex, cargo.pop())
        insertionIndex+=2
for i in range(0, len(cargo)):
        print(cargo[i], end =" ")  
