# circular linked list
# ****insert at position****

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beginning(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
    def insert_pos(self,pos,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            if pos==1:
                insert_beginning(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node
    def display(self):
        if self.head is None:
            print("Circular Linked list is empty")
        else:
            temp=self.head #temp=first node
            print(temp.data,end=" -> ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,end="->")
            print(temp.next.data)
obj=cll()
node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node5=node(50)
node6=node(60)
obj.head=node1
obj.tail=node1
obj.tail.next=obj.head
#print(obj.tail.next)
node1.next=node2
obj.tail=node2
obj.tail.next=obj.head
#print(node1.next)
#print(obj.tail.next)
#print(node2.next)
node2.next=node3
obj.tail=node3
obj.tail.next=obj.head
#print(obj.tail.next)
node3.next=node4
obj.tail=node4
obj.tail.next=obj.head
#print(obj.tail.next)
node4.next=node5
obj.tail=node5
obj.tail.next=obj.head
#print(obj.tail.next)
node5.next=node6
obj.tail=node6
obj.tail.next=obj.head
#print(obj.tail.next)
obj.display()
print()
#obj.insert_beginning()
#obj.display()
obj.insert_pos(3,90)
obj.display()