# Paradiso Application
# Powerful for finding shortest path in the warehouses
# Modified TSP problem
# authors: Amir Zargari, Marzieh Ashrafi, Amir Aqajari

import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import *
from Main_menu import *
from DataBase import *
from Initialize_Map import Initialize_Map

'''
app = QtGui.QApplication(sys.argv) # make UI
MainWindow = QtGui.QMainWindow()
main_menu = MainMenu()
main_menu.show()
sys.exit(app.exec_())
'''
# With out login

app1 = QtGui.QApplication(sys.argv) # make UI
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow, LocMat.shape[0], LocMat.shape[1])
Initialize_Map(ui) # show shelves on map
MainWindow.show()
sys.exit(app1.exec_())

