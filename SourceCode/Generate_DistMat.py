from Show_Path import bfs
from DataBase import *
import numpy as np

def Generate_DistMat ():
    f = open("PathResult.txt","w+")
    rows = len(LocMat)
    columns = len(LocMat[1])
    for row in xrange(0,rows):
        for column in xrange(0,columns):
            if (int(LocMat[row,column]) == 0):
                for r in xrange(0,rows):
                    for c in xrange(0,columns):
                        if (int(LocMat[r,c]) == 0):
                            path = bfs(LocMat, (row,column), (r,c))
                            f.write("%d\t%d\t%d\t%d\t%d" %(row,column, r,c, len(path)-1))
                            #f.write(" ")
                            #f.write("%s" %(path))
                            f.write("\n")
    f.close()

def Matrix_Generator ():
    file = open("PathResult.txt", "r")
    rows = len(LocMat)
    columns = len(LocMat[1])
    DistMat = np.zeros((rows,columns,rows,columns))

    for line in file:
        values = line.split("\t")
        DistMat[int(values[0])][int(values[1])][int(values[2])][int(values[3])] = int(values[4])
    file.close()
    np.save("DistMat.npy", DistMat)

def Find_in_Matrix (start, end):
    DistMat = np.load("DistMat.npy")
    return DistMat[start[0]][start[1]][end[0]][end[1]]
