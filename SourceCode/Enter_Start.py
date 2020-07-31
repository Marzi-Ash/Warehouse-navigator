from DataBase import LocMat
from PyQt4 import QtCore, QtGui

def Enter_Start(row, column, ui):
    StartLoc = [row,column]
    print StartLoc
    StartLoc_show= [column,ui.rows-row-1]
    # Check if start point is valid or not
    if ((0 <= StartLoc[0] and StartLoc[0] < len(LocMat)) and
        (0 <= StartLoc[1] and StartLoc[1] < len(LocMat[0])) ):
        if ((LocMat[StartLoc[0], StartLoc[1]] == 0)):
            print "Your starting point is: ", StartLoc
            message = "Your starting point is: " + str(StartLoc_show)
            # show the valid start point on map
            item = QtGui.QTableWidgetItem("S")
            item.setBackground(QtCore.Qt.cyan)
            ui.Map.setItem(row, column, item)
            ui.valid_start = True
            if (ui.valid_end == True and ui.end[0] == StartLoc[0] and ui.end[1] == StartLoc[1]):
                item = QtGui.QTableWidgetItem("S E")
                item.setBackground(QtCore.Qt.cyan)
                ui.Map.setItem(row, column, item)

        else:
            print "The point you entered is located on shelves"
            print "Please enter a valid location ..."
            message = "The point you entered is located on shelves \n" + "Please enter a valid location ..."
            ui.valid_start = False

    else:
        print "The point you entered is out of range"
        print "Please enter a valid location ..."
        message = "The point you entered is out of range \n" + "Please enter a valid location ..."
        ui.valid_start = False

    # show message on map
    ui.textEdit.setText(message)
