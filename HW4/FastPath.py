n = 0
def main():
    global n
    n = input()
    n = int(n)
    for i in range(0, n):
        time = 0
        data = input().split()
        N=0
        S=0
        E=0
        W=0
        for j in range(0, len(data)):
            if data[j]=='N':
                N+=1
            elif data[j]=='S':
                S+=1
            elif data[j]=='E':
                E+=1
            elif data[j]=='W':
                W+=1
        mapSki = []
        row=[]
        for x in range(0, E+W):
            row.append(0)
        for y in range(0, N+S):
            mapSki.append(row.copy())




if __name__ == "__main__":
    main()
