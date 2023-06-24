class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
class Tree_ds:
    def __init__(self):
        self.root=None
node_1=Node(20)
node_2=Node(30)
node_3=Node(40)
node_4=Node(50)
node_5=Node(60)
node_6=Node(70)
node_7=Node(80)
tree=Tree_ds()
tree.root=node_1
node_1.r_child=node_2
node_1.l_child=node_3
node_2.r_child=node_4
node_2.l_child=node_5
node_3.r_child=node_6
node_3.l_child=node_7
print(tree.root)
print(node_1.data)
print(node_1.r_child.data)
print(node_1.l_child.data)
print(node_2.r_child.data)
print(node_2.l_child.data)
print(node_3.r_child.data)
print(node_3.l_child.data)

