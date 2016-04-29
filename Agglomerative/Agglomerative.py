#Agglomerative

import node.py

def agglomerativeClustering(matrix):



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
