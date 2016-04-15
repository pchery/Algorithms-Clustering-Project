
import random



# def kmeans(A, k):
#
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

print distance(1,5,2,6)

def averageLocation(A):
    sumX = sumY =  0
    for (x,y) in A:
        sumX += x
        sumY += y
    averageX = sumX / len(A)
    averageY = sumY / len(A)
    return averageX ,averageY


def generateCentroids(k, s):
    A = []
    for i in (0 , k):
        A[i] = (int(random.random() * s), int(random.random() * s))


print averageLocation([(1,2), (1,1)])
print generateCentroids(3, 5)