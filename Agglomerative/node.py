
class Node:
    def __init__(self, value, leftChild, rightChild):
        self.value = value;
        self.leftChild = leftChild;
        self.rightChild = rightChild;
        if(self.leftChild == None or self.rightChild == None):
           self.numLeaves = 1
        else:
            self.numLeaves = leftChild.numLeaves + rightChild.numLeaves;


    def hasChildren(self):
        if(self.rightChild != None and self.leftChild != None):
            return True
        else:
            return False






def getLeaves(tree):
    if(tree.rightChild == None and tree.leftChild == None):
        return [tree.value]
    return getLeaves(tree.leftChild) + getLeaves(tree.rightChild)


rightChild = Node(12, None, None)
leftChild = Node(11, None, None)
x = Node(15, leftChild,rightChild)
y = Node(10, x,x)
z = Node(2, y,x)

# print(x.leftChild.value)
# print(x.rightChild.value)
print getLeaves(z)