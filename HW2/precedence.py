stack = []
def addPrecedence(work):
        stack.append(work)

def work(sec):
        if len(stack)==0:
                print("main")
                return
        while sec!=0 :
                if len(stack)==0:
                        print("main")
                        return
                stack[len(stack)-1][1]-=1
                if stack[len(stack)-1][1]==0:
                        stack.pop()
                sec-=1
        if len(stack)==0:
                print("main")
                return
        
        print(stack[len(stack)-1][0])

def main():
        numCommands = int(input())
        while numCommands!=0:
                string = input().split()
                if string[0]=="t":
                        work(int(string[1]))
                else:
                        precedence = []
                        precedence.append(string[0])
                        precedence.append(int(string[1]))
                        addPrecedence(precedence)
                numCommands-=1
main()