
class Node:
    def __init__(self, value, leftChild, rightChild):
        self.value = value;
        self.leftChild = leftChild;
        self.rightChild = rightChild;





rightChild = Node(12, None, None)
leftChild = Node(11, None, None)
x = Node(15, leftChild,rightChild)

print(x.leftChild.value)
print(x.rightChild.value)