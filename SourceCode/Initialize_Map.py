import numpy as np
from PyQt4 import QtCore, QtGui
from DataBase import LocMat

def Initialize_Map (ui):
	rows = len(LocMat)
	columns = len(LocMat[1])
	for row in xrange(0,rows):
		for column in xrange(0,columns):
			if (int(LocMat[row,column]) == 1):
				# show shelves with red color on map
				item = QtGui.QTableWidgetItem()
				item.setBackground(QtCore.Qt.darkRed)
				ui.Map.setItem(row, column, item)
			elif (int(LocMat[row,column]) == 0):
				# show empty location in white color on map
				item = QtGui.QTableWidgetItem()
				item.setBackground(QtCore.Qt.white)
				ui.Map.setItem(row, column, item)
