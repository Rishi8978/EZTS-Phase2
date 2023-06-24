# **** insert at position****
class Node:
    def __init__(self,data):
        self.previous=None
        self.data=data
        self.next=None

class Dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("double ll  is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
    def  insert_pos(self,pos,data):
        new_Node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_Node.previous=temp
        new_Node.next=temp.next
        temp.next.prev=new_Node
        temp.next=new_Node
Node_1=Node("Rishika")
Node_2=Node("asha")
Node_3=Node("anu")
dl=Dll()
dl.head=Node_1
Node_1.next=Node_2
Node_2.previous=Node_1
Node_2.next=Node_3
Node_3.previous=Node_2
print(Node_1.data)
print(Node_2.data)
print(Node_3.data)
#print(Node_1)
#print(Node_2)
#print(Node_3)
#print(Node_1.next)
#print(Node_2.previous)
#print(Node_2.next)
#print(Node_3.previous)
dl.insert_pos(2,"sam")
dl.display()