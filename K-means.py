import random
import math


#def kmeans(A, k):


#     Forgy method: randomly choose k observations as centroids
#     Randome partitioning: randomly assigns a cluster to each observation
#     #get random centroids
#
#     #repeat{
#     #assign all data points to a centroid that is closest to it
#
#     #move centroids to average location of points closest to it
# return centroid

def distance(x,y, a, b):
    dx = x - a
    dy = y - b
    distance = ((dx**2) + (dy**2))**0.5
    return distance

def distanceD(d, A,B):
    distance = 0
    for i in range(0,d):
        distance += (A[i] - B[i])**2
    return distance**0.5


#print distance(1,5,2,6)

def averageLocation(d, matrix):
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
    print("math ", int(math.ceil(1.66)))
    centroidVectors = []
    random.shuffle(matrix)
    print matrix
    for i in range(0,k):
        lo = int(math.ceil(float(d)/k)*(i))
        print "lo", lo
        hi = int(math.ceil(float(d)/k)*(i+1))
        print "hi", hi
        # if ((i == k - 1) and d%k != 0):
        #     hi += 1
        centroids.append(averageLocation(3, matrix[lo:hi]))
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




#print averageLocation([(1,2), (1,1)])
#print generateCentroids(3, 5)
#print(distanceD(2, [0,0], [1,0]))
#print(distanceD(2, [0,0], [1,1]))
#print(distanceD(3, [0,0,0], [1,1,1]))

#print(averageLocation(3, [[0,0,0],[1,1,1], [1,1,1]]))

print(generateCentroids(2, [[1,1,1],[2,2,2], [3,3,3], [1,1,1],[2,2,2]]))

#print(generateCentroids(3, [[1,1,1],[2,2,2],[1,1,1],[2,2,2],[3,3,3],[3,3,3]]))

#print(generateCentroids(4, [[1,1,1],[2,2,2],[1,1,1],[2,2,2],[3,3,3],[3,3,3],[4,4,4],[4,4,4]]))