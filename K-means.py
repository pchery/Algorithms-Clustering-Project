"""
Paul Chery, Scott Pedersen and Mack Hartley
Clustering Project
COMP 221
May 7, 2016

This file contains our code corresponding to our implementation of the k-means
algorithm. If you want to run kmeans on your own data set, call 

kmeans(k, matrix)

where k is the number of clusters you want generated and matrix is a n x d 
matrix, or an array of n d-dimensional vectors. The fuction will return a 
tuple of the list of centroids generated and a dictionary. The dictionary has
vectors as the keys for the index (in the list of centroids) that corresponds
to that vector. 

"""

import random
import math
from dataManipulation import getNameOfCereal


def kmeans(k, matrix):
    """This function takes in an integer K and a list of vectors MATRIX. 
    It then groups them into groups of len(MATRIX) / K vectors and returns 
    a tuple of a list of the generated centroids and a dictionary that holds
    a vector and the index of the centroid it corresponds to as the value."""
    centroids = generateCentroids(k, matrix)
    masterDict = {}
    for i in range(k):
        masterDict[i] = []  #(keys, values)
    previousCentroids = []
    j = 0
    while previousCentroids != centroids: #Continues until the centroids have settled
        for i in range(len(matrix)):
            previousCentroids = centroids
            closestCentroidIndex = findClosestCentroid(matrix[i], centroids) #Gets closest cent
            masterDict[closestCentroidIndex].append(matrix[i])
        for i in range(len(centroids)): #Obtains the average locations of the centroids
            if(centroids[i] != []):
                centroids[i] = averageLocation(masterDict[i])
    print (centroids)
    print (masterDict)
    return masterDict


def distance(A,B):
    """This function takes in two vectors A and B and returns the euclidean 
    distance between the two points in len(A) space. A and B must be the 
    same length. """
    d = len(A)
    distance = 0
    for i in range(0,d): #Calculates distance for any dimention
        distance += (A[i] - B[i])**2
    return distance**0.5


#print distance(1,5,2,6)

def averageLocation(matrix):
    """This function takes in an array of vectors and returns a vector where
    each element is the average of that element from every vector in the input
    array MATRIX. """
    d = len(matrix[0]) #Number of dimensions
    B = [0] * d #Return array
    for vector in matrix:
        for i in range(0, d):
            B[i] += vector[i] #Calculates return vector
    for k in range(0, d):
        B[k] /= float(len(matrix))
    return B


def generateCentroids(k, matrix):
    """This function takes in a positive integer K and an array of vectors 
    MATRIX. It then randomly generates K centroids calculated from approximately
    the same number of vectors. """
    centroids = []
    d = len(matrix) #Obtains dimension of vectors
    random.shuffle(matrix)
    for i in range(0,k):
        lo = int(math.ceil(float(d)/k)*(i)) #Calculates for random location
        hi = int(math.ceil(float(d)/k)*(i+1))
        if(matrix[lo:hi] != []):
            centroids.append(averageLocation(matrix[lo:hi])) #Sets new location
        d = len(matrix)
    return centroids #Returns randomly generated centroids


def findClosestCentroid(vector, centroids):
    """This function takes in a vector VECTOR and a list of centroids CENTROIDS
    and returns the index of the centroid with the smallest euclidean distance
    from VECTOR. """
    closestCentroid = centroids[0]
    closestCentroidIndex = 0; #Initialize the index of the closest centroid to first
    closestDistance = distance(vector, closestCentroid)
    for i in  range (1, len(centroids)): #Iterate through centroids
        currentDistance = distance(vector, centroids[i])
        if closestDistance > currentDistance: #If a closer centroid is found, update
            closestDistance = currentDistance
            closestCentroid = centroids[i]
            closestCentroidIndex = i
    return closestCentroidIndex #Return index of closest centroid



#print averageLocation([(1,2), (1,1)])
#print generateCentroids(3, 5)
#print(distanceD(2, [0,0], [1,0]))
#print(distanceD(2, [0,0], [1,1]))
#print(distanceD(3, [0,0,0], [1,1,1]))

#print(averageLocation(3, [[0,0,0],[1,1,1], [1,1,1]]))

# print(kmeans(3, [[2,2,2],[2,2,2], [4,4,4],[6,6,6]]))

#Manually generated data set for testing
kellogMatrix = [
    [0.1818, 0.6, 0.3333, 0.8125, 0.6429, 0.0000, 0.3333, 1.0, 0.9677, 0.0],
    [0.0000,  0.6, 0.0000, 0.4375, 1.0000, 0.0667, 0.0000, 1.0, 1.0000, 0.0],
    [0.5455,  0.2, 0.0000, 0.3906, 0.0714, 0.2667, 0.9333, 0.5, 0.0323, 0.0],
    [0.4545,  0.2, 0.0000, 0.9063, 0.0714, 0.9333, 0.1333, 0.0, 0.0484, 0.0],
    [0.5455,  0.0, 0.0000, 0.2813, 0.0714, 0.4000, 0.8000, 0.5, 0.0000, 0.0],
    [0.5455,  0.4, 1.0000, 0.4375, 0.2857, 0.2000, 0.4667, 1.0, 0.4516, 0.0],
    [0.5455,  0.2, 0.0000, 0.6875, 0.0714, 0.9333, 0.2000, 1.0, 0.0323, 0.0],
    [0.5455,  0.2, 0.3333, 0.3906, 0.0714, 0.2667, 0.8667, 0.5, 0.0323, 0.0],
    [0.5455,  0.0, 0.0000, 0.6250, 0.0714, 0.4667, 0.7333, 0.0, 0.0161, 0.0],
    [0.4545,  0.4, 0.0000, 0.0000, 0.2143, 0.4667, 0.4667, 0.5, 0.2581, 0.0],
    [0.6364,  0.4, 0.0000, 0.7500, 0.3571, 0.4667, 0.8000, 1.0, 0.5484, 0.0],
    [0.5455,  0.2, 0.3333, 0.5313, 0.0714, 0.6667, 0.4000, 1.0, 0.1290, 1.0],
    [0.8182,  0.4, 0.3333, 0.5313, 0.1429, 0.8667, 0.6000, 1.0, 0.2419, 1.0],
    [1.0000,  0.4, 0.6667, 0.4688, 0.2143, 0.6667, 0.8667, 1.0, 0.4516, 0.0],
    [0.6364,  0.2, 0.3333, 0.5938, 0.0000, 0.5333, 0.6000, 0.5, 0.0645, 0.0],
    [0.8182,  0.4, 0.6667, 0.6875, 0.2143, 0.9333, 0.4667, 1.0, 0.3548, 0.0],
    [0.3636,  0.4, 0.0000, 0.5313, 0.2143, 0.7333, 0.1333, 1.0, 0.2258, 0.0],
    [0.4545,  0.4, 0.0000, 1.0000, 0.0714, 0.8667, 0.2000, 1.0, 0.0806, 1.0],
    [0.6364,  0.4, 0.3333, 0.6563, 0.3571, 0.4667, 0.8000, 0.5, 0.7097, 0.0],
    [0.3636,  0.2, 0.0000, 0.0000, 0.1429, 0.5333, 0.4000, 1.0, 0.2903, 0.0],
    [0.5455,  0.2, 0.0000, 0.9063, 0.0000, 1.0000, 0.2000, 0.0, 0.0484, 0.0],
    [0.5455,  0.2, 0.3333, 0.2188, 0.0714, 0.1333, 1.0000, 0.5, 0.0645, 0.0],
    [0.5455,  1.0, 0.0000, 0.7188, 0.0714, 0.6000, 0.2000, 0.0, 0.1129, 0.0]]


dict = kmeans(5, kellogMatrix)
for k in range(0, 5):
    print("CLUSTER " + str(k) + " : ")
    for i in range (len(dict[k])):
        print (getNameOfCereal(dict[k][i]))



