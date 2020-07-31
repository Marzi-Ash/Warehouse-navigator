'''
Branch and bound algorithm

modified version of gitHub@MostafaBahri
'''
from utility import Node, PriorityQueue
import numpy as np
from DataBase import DistMat
from PyQt4 import QtCore, QtGui
import time

def Branch_Bound (ui):
    time_out = 0
    start_time = time.time() # for time out

    initial_order = []
    for i in ui.list_order_loc:
        initial_order.append((i[0]-1,i[1]))

    first_order = initial_order
    first_order.append(ui.end)
    first_order = [ui.start]+first_order
    adj_mat = np.zeros((len(first_order),len(first_order)))

    for i in xrange(0,len(first_order)):
        for j in xrange (0,len(first_order)):
            if (i == j):
                adj_mat[i][j] = float("inf")
            else:
                 adj_mat[i][j] = DistMat[first_order[i][0],first_order[i][1],first_order[j][0],first_order[j][1]]
    src = 0
    end = len(first_order)-1

    optimal_tour = []
    n = len(adj_mat)
    if not n:
        raise ValueError("Invalid adj Matrix")
    u = Node()
    PQ = PriorityQueue()
    optimal_length = 0
    v = Node(level=1, path=[end, src])
    min_length = float('inf')  # infinity
    v.bound = bound(adj_mat, v)
    PQ.put(v)

    while not PQ.empty():
        if (time.time()-start_time > 55): # 1 MIN time out
            print ("time out")
            time_out = 1
            return [],[],time_out
        v = PQ.get()
        #print v.path
        if v.bound < min_length:
            u.level = v.level + 1
            for i in filter(lambda x: x not in v.path, range(1, n)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == n - 2:
                    l = set(range(0, n)) - set(u.path)
                    u.path.append(list(l)[0])
                    u.path.append(end)
                    _len = length(adj_mat, u)
                    if _len < min_length:
                        min_length = _len
                        optimal_length = _len
                        optimal_tour = u.path[:]

                else:
                    u.bound = bound(adj_mat, u)
                    if u.bound < min_length:
                        PQ.put(u)
                # make a new node at each iteration! python it is!!
                u = Node(level=u.level)

    # shifting to proper source(start of path)
    exec_time = time.time()-start_time
    print "Exec time for Branch and Bound is %s" %exec_time

    optimal_tour_src = optimal_tour
    #if src is not 1:
    optimal_tour_src = optimal_tour[:-1]
    y = optimal_tour_src.index(src)
    optimal_tour_src = optimal_tour_src[y:] + optimal_tour_src[:y]
    #optimal_tour_src.append(optimal_tour_src[0])
    optimal_length = optimal_length - adj_mat[src][end] #removing src to end

    loc_optimal_tour_src = []

    for order in optimal_tour_src:
        loc_optimal_tour_src.append(first_order[order])

    return  optimal_length, loc_optimal_tour_src, time_out


def length(adj_mat, node):
    tour = node.path
    # returns the sum of two consecutive elements of tour in adj[i][j]
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in xrange(len(tour) - 1)])


def bound(adj_mat, node):
    path = node.path
    _bound = 0

    n = len(adj_mat)
    determined, last = path[:-1], path[-1]
    # remain is index based
    remain = filter(lambda x: x not in path, range(n))

    # for the edges that are certain
    for i in xrange(len(path) - 1):
        _bound += adj_mat[path[i]][path[i + 1]]

    # for the last item
    _bound += min([adj_mat[last][i] for i in remain])

    p = [path[0]] + remain
    # for the undetermined nodes
    for r in remain:
        _bound += min([adj_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound
