import numpy as np
from DataBase import DistMat
from PyQt4 import QtCore, QtGui
from itertools import permutations
from Prim import prims
import time


def Modified_Brute_Force(ui):
    start_time = time.time()
    #initial minimum
    #upper bound
    initial_order = []
    for i in ui.list_order_loc:
        initial_order.append((i[0]-1,i[1]))
    perm = permutations(initial_order)
    # For Bruthe force
    first_order = initial_order
    first_order.append(ui.end)
    first_order = [ui.start]+first_order
    Dist = 0
    optimal = first_order
    graph = []
    print "first Order = %s" %optimal
    for i in range(0,len(optimal)-1):
        for j in range(i+1,len(optimal)):
            if (i==0 and j==len(optimal)):# we do not have path between start and end directly
                continue
            graph.append([i,j,DistMat[optimal[i][0],optimal[i][1],optimal[j][0],optimal[j][1]]])

    mst,total_mst = prims(len(optimal), graph)
    print "mst = %s" %mst
    #print "total_mst = %s" %total_mst


    for i in range(0,len(first_order)):
        if i != len(first_order)-1:
            Dist = Dist + DistMat[first_order[i][0],first_order[i][1],first_order[i+1][0],first_order[i+1][1]]

    terminate = 1.05+(float(len(first_order)-2))/20

    for l in perm:
        order = list(l)
        order.append(ui.end)
        order = [ui.start]+order
        this_order_dist = 0
        for i in range(0,len(order)):
            if i != len(order)-1:
                this_order_dist = this_order_dist + DistMat[order[i][0],order[i][1],order[i+1][0],order[i+1][1]]
        if (this_order_dist < Dist):
            Dist = this_order_dist
            optimal = order
        if Dist < terminate * total_mst:
            break
    #print "optimal = %s" %Dist
    #print "optimal = %s" %optimal
    exec_time = time.time()-start_time

    print "Exec time for modified brute force is %s" %exec_time

    return Dist,optimal
