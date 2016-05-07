"""
Paul Chery, Scott Pedersen and Mack Hartley
Clustering Project
COMP 221
May 7, 2016

This file contains our code corresponding to the class Node that we used
when implementing an agglomerative clustering algorithm. Nodes are meant to
contain a vector as a value, as well as a left child and a right child and 
the number of leaves beneath itself on the tree. 

"""

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
        """This function returns TRUE if the node has children, and false if
        it does not. """
        if(self.rightChild != None and self.leftChild != None):
            return True
        else:
            return False






def getLeaves(tree):
    """This function returns an array of the leaves corresponding to the root
    of an inputted tree TREE. """
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
print (getLeaves(z))