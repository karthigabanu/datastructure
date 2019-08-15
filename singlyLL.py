class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insertatbeg(self,data):
        new=Node(data)
        new.nxt=self.head
        self.head=new

    def inseratmid(self,mid,data):
        if mid is None:
            print("node is absent")
            return
        new=Node(data)
        new.next=mid.next
        mid.nxt=new
    
    def insertatend(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        last=self.head
        while(last.next):
            last=last.next
            last.next=newnode

    def deleteatbegin(self, data):
        new=Node(data)
        new.next=self.head
        self.head=new
    

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,'==>',end='')
            temp=temp.next
        
obj=linkedlist()
ch=0
while ch!=6:
    print("*singly linked list*\n","1.Insert at begin 2.Insert at mid 3.Insert at end 4.Deletion 5. printlist ")
    ch=int(input())
    if ch==1:
        print("enter the value:")
        data=input()
        obj.insertatbeg(data)
        obj.printlist()
    elif ch==2:
        print("enter the value:")
        data=input()
        mid=input("enter the value:")
        obj.insertatmid(mid,data)
        obj.printlist()
    elif ch==3:
        print("enter the value:")
        data=input()
        obj.insertatend(data)
        obj.printlist()
    elif ch==4:
        obj.delAtBeg()
        obj.printList()
   
    elif ch==5:
        obj.printlist()
    
