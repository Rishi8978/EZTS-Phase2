# **** DELETE AT BEGINING****
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=SLL()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
print("")
obj.delete_beginning()
obj.display()
print("")