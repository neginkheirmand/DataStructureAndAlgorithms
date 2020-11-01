#if Ur asking about the file name : i just wanted to make it look fun
def main():
        inputString = input().split()
        cargo = []
        newCargo = []
        for i in range(0, len(inputString)):
                cargo.append(int(inputString[i]))
        if len(cargo)==1:
                print(cargo[0])
                return
        if len(cargo)==0:
                return
        newCargo.insert(0, cargo.pop())
        newCargo.append(cargo[0])
        i=1
        while i<len(cargo):
                # print(cargo)
                # print(newCargo)
                newCargo.append(cargo.pop())
                if i<len(cargo):
                        newCargo.append(cargo[i])
                i+=1

        for i in range(0, len(newCargo)):
                print(newCargo[i], end =" ")  

main()