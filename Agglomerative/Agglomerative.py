#Agglomerative

from node import *
from scottPecans import *
import sys



def agglomerativeClustering(data, k):
    data = dataToNodeList(data)
    while len(data) > k:
        minDistance = sys.maxint
        minNodes = Node(0, None, None), Node(0, None, None)
        for i in range(len(data)):
            for j in range (i+1, len(data)):
                if (distance(data[i].value, data[j].value) < minDistance):
                    minDistance = distance(data[i].value, data[j].value)
                    minNodes = data[i], data[j]
        data.remove(minNodes[0])
        data.remove(minNodes[1])
        parent = Node(averageLocation([minNodes[0], minNodes[1]]), minNodes[0], minNodes[1])
        data.append(parent)
    for i in range(len(data)):
        data[i] = getLeaves(data[i])
    return data


#
# def treeToArray(data):
#     vectorDict = {}
#     for i in len(data):
#         node = data[i]
#         while(node.hasChildren()):


def dataToNodeList(data):
    A = []
    for vector in data:
        A.append(Node(vector, None,None))
    return A


#make every point into cluster
#find closest points and merge them
#continue until you have a tree


#plot dendogram

def distance(A,B):
    d = len(A)
    distance = 0
    for i in range(0,d):
        distance += (A[i] - B[i])**2
    return distance**0.5


def averageLocation(nodeTuple):
    d = len(nodeTuple[0].value)
    B = [0] * d
    for node in nodeTuple:
        for i in range(0, d):
            B[i] += node.value[i] * node.numLeaves
    for k in range(0, d):
        B[k] /= (nodeTuple[0].numLeaves + nodeTuple[1].numLeaves)
    return B


print(agglomerativeClustering(kellogMatrix, 5))


result = agglomerativeClustering(kellogMatrix, 6)
for k in range(0, 6):
    print("CLUSTER " + str(k) + " : ")
    for i in range (len(result[k])):
        print getNameOfCereal(result[k][i])