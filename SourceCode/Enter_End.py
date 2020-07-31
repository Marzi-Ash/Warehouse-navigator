from DataBase import LocMat
from PyQt4 import QtCore, QtGui

def Enter_End(row, column, ui):
    EndLoc = [row,column]
    EndLoc_show= [column,ui.rows-row-1]
    print EndLoc
    # Check if end point is valid or not
    if ((0 <= EndLoc[0] and EndLoc[0] < len(LocMat)) and
        (0 <= EndLoc[1] and EndLoc[1] < len(LocMat[0])) ):
        if ((LocMat[EndLoc[0], EndLoc[1]] == 0)):
            print "Your ending point is: ", EndLoc
            message = "Your ending point is: " + str(EndLoc_show)
            # Show valid input on map
            item = QtGui.QTableWidgetItem("E")
            item.setBackground(QtCore.Qt.cyan)
            ui.Map.setItem(row, column, item)
            ui.valid_end = True

            if (ui.valid_start == True and ui.start[0] == EndLoc[0] and ui.start[1] == EndLoc[1]):
                item = QtGui.QTableWidgetItem("S E")
                item.setBackground(QtCore.Qt.cyan)
                ui.Map.setItem(row, column, item)

        else:
            print "The point you entered is located on shelves"
            print "Please enter a valid location ..."
            message = "The point you entered is located on shelves \n" + "Please enter a valid location ..."
            ui.valid_end = False

    else:
        print "The point you entered is out of range"
        print "Please enter a valid location ..."
        message = "The point you entered is out of range \n" + "Please enter a valid location ..."
        ui.valid_end = False

    # show message on map
    ui.textEdit.setText(message)
