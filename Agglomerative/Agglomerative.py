"""
Paul Chery, Scott Pedersen and Mack Hartley
Clustering Project
COMP 221
May 7, 2016

This file contains our code for our implementation of Agglomerative 
clustering. If you want to run our implementation on your own data set,
call

agglomerativeClustering(data, k)

where k is the number of clusters you want generated and matrix is a n x d 
matrix, or an array of n d-dimensional vectors. The function will return a 
length k array, where each element of k corresponds to a list of vectors that
were clustered together by the algorithm. 

"""
from node import *
from dataManipulation import *
import sys



def agglomerativeClustering(data, k):
    """This function takes in a a list of vectors DATA and the number of
    clusters K we want to split DATA into. The function will return a 
    length k array, where each element of k corresponds to a list of vectors 
    that were clustered together by the algorithm. """
    data = dataToNodeList(data) #Converts our data to a list of nodes
    while len(data) > k:
        minDistance = sys.maxint #Initialize min dist to inf
        minNodes = Node(0, None, None), Node(0, None, None)
        for i in range(len(data)): #This double for loop checks for closest nodes
            for j in range (i+1, len(data)):
                if (distance(data[i].value, data[j].value) < minDistance):
                    minDistance = distance(data[i].value, data[j].value)
                    minNodes = data[i], data[j] #Stores the two nodes that are closest
        data.remove(minNodes[0]) #Removes old two closest nodes
        data.remove(minNodes[1])
        parent = Node(averageLocation([minNodes[0], minNodes[1]]), minNodes[0], minNodes[1]) #Creates new node, representing a new cluster
        data.append(parent)
    for i in range(len(data)):
        data[i] = getLeaves(data[i]) #Gets leaves of the data where cluster items are stored
    return data

def dataToNodeList(data):
    """This function takes in a list of vectors DATA and returns a list where
    each element is the root of a tree with no children with a value of some 
    vector from data. """
    A = []
    for vector in data:
        A.append(Node(vector, None,None)) #Creates our return array A of nodes
    return A

def distance(A,B):
    """This fucntion takes in two vectors A and B and return the euclidean
    distance between them in len(A) space. A and B are the same length. """
    d = len(A)
    distance = 0
    for i in range(0,d): #Calculates the distance for any set of dimensions
        distance += (A[i] - B[i])**2
    return distance**0.5


def averageLocation(nodeTuple):
    """This function takes in a tuple of two nodes that hold nodes that 
    are the roots of a tree where the leaves are vectors. The root contains 
    the centroid of the leaves as its value. The function returns the centroid
    for the leaves of both of these roots. """
    d = len(nodeTuple[0].value) #Number of dimensions
    B = [0] * d #Return array
    for node in nodeTuple:
        for i in range(0, d):
            B[i] += node.value[i] * node.numLeaves #Calculates the return location
    for k in range(0, d):
        B[k] /= (nodeTuple[0].numLeaves + nodeTuple[1].numLeaves)
    return B


print(agglomerativeClustering(kellogMatrix, 5))


result = agglomerativeClustering(kellogMatrix, 6)
for k in range(0, 6):
    print("CLUSTER " + str(k) + " : ")
    for i in range (len(result[k])):
        print (getNameOfCereal(result[k][i]))