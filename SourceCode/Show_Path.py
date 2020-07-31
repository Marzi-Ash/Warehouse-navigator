import numpy as np
import collections
from DataBase import LocMat
from PyQt4 import QtCore, QtGui

def Show_Path(start,end,ui):
    path = bfs(LocMat, start, end) # Call BFS from start to product
    Print_Direction(path, ui)
    for (x,y) in path:
        # Show path on map
        item = QtGui.QTableWidgetItem("")
        item.setBackground(QtCore.Qt.green)
        ui.Map.setItem(x, y, item)
    return path

def bfs(grid, start, goal):
    # implemention of bfs using queue
    queue = collections.deque([[start]]) # contains of paths
    seen = set([start])
    row = grid.shape[0]
    column = grid.shape[1]
    while queue:
        path = queue.popleft()
        x, y = path[-1] # the last onw
        if (x,y) == goal:
            break
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if (0 <= x2 < row and 0 <= y2 < column and grid[x2][y2] != 1 and (x2, y2) not in seen):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return path

def Print_Direction(path_computer_cordinate, ui):
    path = path_computer_cordinate
    path = []
    for p in path_computer_cordinate:
        path.append((p[1],ui.rows-p[0]-1))
    print "path used for print direction is"
    print path
    ui.textEdit.setText("The length of total path to collect all product is %s\n" %(ui.Dist))
    north = False
    east = False
    south = False
    west = False
    num = 0
    for i in range(len(path)-1):
        if path[i][0] == path[i+1][0]:
            # x is fixed
            # north or south
            if east == True:
                print "Go %d steps east from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
                ui.textEdit.append("Go %d steps east from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
                east = False
                num = 0

            if west == True:
                print "Go %d steps west from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
                ui.textEdit.append("Go %d steps west from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
                west = False
                num = 0

            if path[i][1] < path[i+1][1]: #north
                if south == True :
                    south = False
                    num = 0
                num = num + 1
                north = True

            if path[i][1] > path[i+1][1]: #south
                if north == True :
                    north = False
                    num = 0
                num = num + 1
                south = True

        elif path[i][1] == path[i+1][1]:
            # y is fixed
            # east or west
            if north == True:
                print "Go %d steps north from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
                ui.textEdit.append("Go %d steps north from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
                north = False
                num = 0

            if south == True:
                print "Go %d steps south from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
                ui.textEdit.append("Go %d steps south from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
                south = False
                num = 0

            if path[i][0] < path[i+1][0]: #east
                if west == True :
                    west = False
                    num = 0
                num = num + 1
                east = True

            if path[i][0] > path[i+1][0]: #west
                if east == True :
                    east = False
                    num = 0
                num = num + 1
                west = True

    i = i + 1
    if north == True:
        print "Go %d steps north from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
        ui.textEdit.append("Go %d steps north from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
    elif east == True:
        print "Go %d steps east from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
        ui.textEdit.append("Go %d steps east from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
    elif south == True:
        print "Go %d steps south from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
        ui.textEdit.append("Go %d steps south from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))
    elif west == True:
        print "Go %d steps west from (%d,%d) to (%d,%d)" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1])
        ui.textEdit.append("Go %d steps west from (%d,%d) to (%d,%d)\n" %(num, path[i-num][0], path[i-num][1], path[i][0], path[i][1]))

#path = [(1,1),(1,2),(1,3),(2,3),(3,3)]
#Print_Direction(path)
