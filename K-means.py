import random
import math
from scottPecans import getNameOfCereal


def kmeans(k, matrix):

    centroids = generateCentroids(k, matrix)
    # vectors = [[]]*len(matrix)
    masterDict = {}
    for i in range(k):
        masterDict[i] = []  #(keys, values)
    # print masterDict
    previousCentroids = []
    j = 0
    while previousCentroids != centroids:
        # j += 1
        # print(j)
        for i in range(len(matrix)):
            previousCentroids = centroids
            closestCentroidIndex = findClosestCentroid(matrix[i], centroids)
            # print closestCentroidIndex
            masterDict[closestCentroidIndex].append(matrix[i])
            # print masterDict
        for i in range(len(centroids)):
            if(centroids[i] != []):
                centroids[i] = averageLocation(masterDict[i])
    return masterDict

#     Forgy method: randomly choose k observations as centroids
#     Randome partitioning: randomly assigns a cluster to each observation
#     #get random centroids
#
#     #repeat{
#     #assign all data points to a centroid that is closest to it
#
#     #move centroids to average location of points closest to it
    return centroid

# def distance(x,y, a, b):
#     dx = x - a
#     dy = y - b
#     distance = ((dx**2) + (dy**2))**0.5
#     return distance

def distance(A,B):
    d = len(A)
    distance = 0
    for i in range(0,d):
        distance += (A[i] - B[i])**2
    return distance**0.5


#print distance(1,5,2,6)

def averageLocation(matrix):
    d = len(matrix[0])
    B = [0] * d
    for vector in matrix:
        for i in range(0, d):
            B[i] += vector[i]
    for k in range(0, d):
        B[k] /= float(len(matrix))
    return B


def generateCentroids(k, matrix):
    centroids = []
    d = len(matrix)
    # print("math ", int(math.ceil(1.66)))
    random.shuffle(matrix)
    # print matrix
    for i in range(0,k):
        lo = int(math.ceil(float(d)/k)*(i))
        #print "lo", lo
        hi = int(math.ceil(float(d)/k)*(i+1))
        #print "hi", hi
        # if ((i == k - 1) and d%k != 0):
        #     hi += 1
        if(matrix[lo:hi] != []):
            centroids.append(averageLocation(matrix[lo:hi]))
        # for i in range(0, d):
        #     centroidVectors.append(matrix[i])
        #     print i
        #     if ((i % (d / k) == 0 and i != 0) or (i == d)):
        #         #print i
        #         centroids.append(averageLocation(3,centroidVectors))
        #         centroidVectors = []
        #random.randint(0, d)
        d = len(matrix)
    return centroids


#NOT TESTED!!!!!!
def findClosestCentroid(vector, centroids):
    closestCentroid = centroids[0]
    closestCentroidIndex = 0;
    closestDistance = distance(vector, closestCentroid)
    for i in  range (1, len(centroids)):
        currentDistance = distance(vector, centroids[i])
        if closestDistance > currentDistance:
            closestDistance = currentDistance
            closestCentroid = centroids[i]
            closestCentroidIndex = i
    return closestCentroidIndex



#print averageLocation([(1,2), (1,1)])
#print generateCentroids(3, 5)
#print(distanceD(2, [0,0], [1,0]))
#print(distanceD(2, [0,0], [1,1]))
#print(distanceD(3, [0,0,0], [1,1,1]))

#print(averageLocation(3, [[0,0,0],[1,1,1], [1,1,1]]))

# print(kmeans(3, [[2,2,2],[2,2,2], [4,4,4],[6,6,6]]))

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
        print getNameOfCereal(dict[k][i])


# print(kmeans(2, kellogMatrix))
#print(generateCentroids(3, [[1,1,1],[2,2,2],[1,1,1],[2,2,2],[3,3,3],[3,3,3]]))

#print(generateCentroids(4, [[1,1,1],[2,2,2],[1,1,1],[2,2,2],[3,3,3],[3,3,3],[4,4,4],[4,4,4]]))