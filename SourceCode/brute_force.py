import numpy as np
from DataBase import DistMat
from PyQt4 import QtCore, QtGui
from itertools import permutations
import time


def Brute_Force(ui):
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

    for i in range(0,len(first_order)):
        if i != len(first_order)-1:
            Dist = Dist + DistMat[first_order[i][0],first_order[i][1],first_order[i+1][0],first_order[i+1][1]]


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
    #print "optimal = %s" %Dist
    #print "optimal = %s" %optimal
    exec_time = time.time()-start_time

    print "Exec time for brute force is %s" %exec_time

    return Dist,optimal
