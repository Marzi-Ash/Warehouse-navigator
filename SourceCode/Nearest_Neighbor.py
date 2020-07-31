import numpy as np
from DataBase import DistMat
from PyQt4 import QtCore, QtGui
from itertools import permutations
from time import sleep
import time

def Nearest_Neighbor(ui):
	start_time = time.time()
	#initial minimum
	#upper bound

	initial_order = []
	for i in ui.list_order_loc:
		initial_order.append((i[0]-1,i[1]))

	first_order = initial_order
	first_order = first_order+[ui.end]
	first_order = [ui.start]+first_order
	Dist = 0
	optimal = first_order
	graph = []
    #print "first Order = %s" %optimal
	for i in range(0,len(optimal)-1):
		for j in range(i+1,len(optimal)):
			if (i==0 and j==len(optimal)):# we do not have path between start and end directly
				continue
			graph.append([i,j,DistMat[optimal[i][0],optimal[i][1],optimal[j][0],optimal[j][1]]])

	for i in range(0,len(first_order)):
		if i != len(first_order)-1:
			Dist = Dist + DistMat[first_order[i][0],first_order[i][1],first_order[i+1][0],first_order[i+1][1]]

	List = initial_order
    #print List
	SmallestCost = float("inf")
	for i in List:
		Order = []
		StartNode = i
		Order.append(StartNode)
		SmallestEdge = float("inf")
		OrderCost = 0
		Terminated = 0
		while(Terminated != 1):
			for j in List:
				if (not j in Order):
					if (DistMat[StartNode[0],StartNode[1],j[0],j[1]] < SmallestEdge):
						SmallestEdge = DistMat[StartNode[0],StartNode[1],j[0],j[1]]
						NextNode = j
            #print SmallestEdge
			Order.append(NextNode)
			#print Order
			OrderCost = OrderCost + SmallestEdge
			SmallestEdge = float("inf")
			StartNode = NextNode
			if (len(Order) == len(List)):
				Terminated = 1
		if (OrderCost < SmallestCost):
			SmallestCost = OrderCost
			FinalOrder = Order

	SmallestCost = SmallestCost + DistMat[ui.start[0],ui.start[1],FinalOrder[0][0],FinalOrder[0][1]]
	SmallestCost = SmallestCost + DistMat[FinalOrder[-1][0],FinalOrder[-1][1],ui.end[0],ui.end[1]]
	FinalOrder = [ui.start]+FinalOrder
	FinalOrder.append(ui.end)
	exec_time = time.time()-start_time
	print "Exec time for Nearest Neighbor algorithm is %s" %exec_time

	if (SmallestCost < Dist):
		Dist = SmallestCost
		optimal = FinalOrder

	return Dist,optimal
