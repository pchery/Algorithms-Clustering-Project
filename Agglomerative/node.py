
class Node:
    def __init__(self, value, leftChild, rightChild):
        self.value = value;
        self.leftChild = leftChild;
        self.rightChild = rightChild;

    def hasChildren(self):
        if(self.rightChild != None and self.leftChild != None):
            return True
        else:
            return False





def traverse(tree, A):
    if(tree.rightChild == None or tree.leftChild == None):
        return tree, []
    else:
        leftNode = traverse(tree.leftChild,A), A
        rightNode = traverse(tree.rightChild,A), A
        A.append(leftNode[0].value, rightNode[0].value)
    return None, A


rightChild = Node(12, None, None)
leftChild = Node(11, None, None)
x = Node(15, leftChild,rightChild)


print(x.leftChild.value)
print(x.rightChild.value)
print traverse(x, [])