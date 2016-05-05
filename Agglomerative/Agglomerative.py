#Agglomerative

from node import Node

def agglomerativeClustering(data, k):
    minDistance = 0
    minNodes = Node(0, None, None), Node(0, None, None)
    while len(data) > 5:
        for i in range(len(data)):
            for j in range (i+1, len(data)):
                if (distance(data(i).value, data(j).value) < minDistance):
                    minDistance = distance(data(i).value, data(j).value)
                    minNodes = data(i), data(j)
        data.remove(minNodes[0])
        data.remove(minNodes[1])
        parent = Node(averageLocation([minNodes[0].value,minNodes[1].value]), minNodes[0], minNodes[1])
        data.add(parent)
    return data

def treeToArray(data):
    vectorDict = {}
    for i in len(data):
        node = data[i]
        while(node.hasChildren())







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


def averageLocation(matrix):
    d = len(matrix[0])
    B = [0] * d
    for vector in matrix:
        for i in range(0, d):
            B[i] += vector[i]
    for k in range(0, d):
        B[k] /= float(len(matrix))
    return B

