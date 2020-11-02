class Node: 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.before = None # Initialize before as null 
		self.after = None

class LinkedList: 
	sizeList=0
	def __init__(self): 
		self.head = None
		self.middleNode = None
		
	def pushToPoshte(self, nodeData):
		self.sizeList+=1
		if self.head == None:
			self.head = Node(nodeData)
			self.middleNode = self.head
			return
		(self.head).after = Node(nodeData)
		((self.head).after).before = self.head
		self.head = (self.head).after
		if self.sizeList%2==1:
			self.middleNode = (self.middleNode).after	
	def pop(self):
		if self.sizeList==0:
			return
		self.sizeList-=1
		if self.sizeList==0:
			self.head = None
			self.middleNode = None
		
		

if __name__=='__main__': 
	poshte = LinkedList()
        inputForm = input().split()
        while inputForm[0]!="finish":
                if inputForm[0]=="push":
                        poshte.pushToPoshte(int(inputForm[1]))
                elif inputForm[0]=="pop":
                        pop()
                elif inputForm[0]=="print":
                        printPoshte()
                elif inputForm[0]=="findMiddle":
                        findMiddleOfPoshte()
                elif inputForm[0]=="removeMiddle":
                        removeMiddleOfPoshte()
                inputForm = input().split()