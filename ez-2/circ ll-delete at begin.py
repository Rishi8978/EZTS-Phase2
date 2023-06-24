#cll- delete at begin

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp.next!=self.head:
                if temp.next is None:
                    temp.next=self.head
                else:
                    print(temp.data,'->',end=' ')
                    temp=temp.next
            print(self.head.data)
    def delete_begin(self):
        if self.head is None:
            print("not exist")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
        
                

obj=circularlinkedlist()
n1=Node(10)
obj.head=n1
obj.tail=n1
obj.tail.next=obj.head
n2=Node(20)
obj.tail=n2
n1.next=n2
n3=Node(30)
obj.tail=n3
n2.next=n3
n4=Node(40)
obj.tail=n4
n3.next=n4
n5=Node(50)
obj.tail=n5
n4.next=n5
n6=Node(60)
obj.tail=n6
n5.next=n6
obj.display()
obj.delete_begin()
obj.display()