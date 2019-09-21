class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.current=None
    def insert(self):
        value=int(input("Enter Node Value"))
        node=Node(value)
        if(self.head==None):
            self.head=node
            self.current=node
        else:
            self.current.next=node
            self.current=node
    def printLL(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"--",end=" ")
            temp=temp.next
        print("None")
LL=LinkedList()
switch={1:LL.insert,2:LL.printLL,3: None}
ch=0
while(ch!=3):
    ch=int(input("1.Enter Node\n2.Print Linked List\n3.Exit \n"))
    switch.get(ch,"Invalid Input")()
    
    
