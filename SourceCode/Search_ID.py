import numpy as np
from DataBase import InputMat, InputFlag, InputFile
from PyQt4 import QtCore, QtGui

def Search_ID(ProductID, ui):
    # check if product ID is valid
    if ProductID in InputMat[:,0]:
        if ProductID in ui.list_order_ID:
            print "Your product is already added"
            message = "Your product is already added"
        else:
            row = np.where(InputMat[:,0] == ProductID)
            first_location=ui.rows-int(InputMat[row,2])-1
            second_location=int(InputMat[row,1])
            print "In our corrdinate The product x location is %d and y location is %d" %(first_location,second_location)
            message = "Your product (x,y) location is (" + str(int(InputMat[row,1]))+","+str(int(InputMat[row,2]))+")"
            # show the specific location of product with yellow
            item = QtGui.QTableWidgetItem("P")
            item.setBackground(QtCore.Qt.yellow)
            ui.Map.setItem(first_location, second_location, item)
            ui.textEdit.setText(message)
            ui.valid_product = True
            ui.list_order_ID.append(ProductID)
            if (((first_location,second_location) in ui.list_order_loc) == 0):
                ui.list_order_loc.append((first_location,second_location))
            # return the location of product
            return(first_location,second_location)
    else:
        ui.valid_product = False
        print "The product you enter is not valid. Please enter a valid product Id ..."
        message = "The product you enter is not valid. Please enter a valid product Id ..."

    # show message on map
    ui.textEdit.setText(message)

def Search_ID_List(ui, next):
    # check if product ID is valid
    ui.map_reset()
    ui.list_order_loc = []
    ui.list_order_ID = []
    if (ui.valid_start == True):
        item = QtGui.QTableWidgetItem("S")
        item.setBackground(QtCore.Qt.cyan)
        ui.Map.setItem(ui.start[0], ui.start[1], item)
    if (ui.valid_end == True):
        item = QtGui.QTableWidgetItem("E")
        item.setBackground(QtCore.Qt.cyan)
        ui.Map.setItem(ui.end[0], ui.end[1], item)
    if (ui.valid_start == True and ui.valid_end == True and ui.start[0] == ui.end[0] and ui.start[1] == ui.end[1]):
        print "salam"
        item = QtGui.QTableWidgetItem("S E")
        item.setBackground(QtCore.Qt.cyan)
        ui.Map.setItem(ui.end[0], ui.end[1], item)
    if (next == 1):
        print "ui.counter = %d" %(ui.counter)
        print InputFlag
        while (True):
            if (InputFlag[0][ui.counter]==1):
                ui.counter = ui.counter + 1
            else:
                for ProductID in InputFile[ui.counter]:
                    if ProductID in InputMat[:,0]:
                        if ProductID in ui.list_order_ID:
                            print "Your product is already added"
                            message = "Your product is already added"
                            ui.textEdit.setText(message)
                        else:
                            row = np.where(InputMat[:,0] == ProductID)
                            first_location=ui.rows-int(InputMat[row,2])-1
                            second_location=int(InputMat[row,1])
                            print "In our corrdinate The product x location is %d and y location is %d" %(first_location,second_location)
                            message = "Your product (x,y) location is (" + str(int(InputMat[row,1]))+","+str(int(InputMat[row,2]))+")"
                            # show the specific location of product with yellow
                            item = QtGui.QTableWidgetItem("P")
                            item.setBackground(QtCore.Qt.yellow)
                            ui.Map.setItem(first_location, second_location, item)
                            ui.textEdit.setText(message)
                            ui.valid_product = True
                            ui.list_order_ID.append(ProductID)
                            if (((first_location,second_location) in ui.list_order_loc) == 0):
                                ui.list_order_loc.append((first_location,second_location))
                            # return the location of product
                            #return(first_location,second_location)
                            ui.textEdit.setText(message)
                    else:
                        ui.valid_product = False
                        print "The product you enter is not valid. Please enter a valid product Id ..."
                        message = "The product you enter is not valid. Please enter a valid product Id ..."
                        ui.textEdit.setText(message)
                InputFlag[0][ui.counter]=1
                ui.counter=ui.counter+1
                ui.textEdit.setText("Your order number is:%d \n" %(ui.counter))
                ui.textEdit.append("Item Added: \n")
                ui.textEdit.append(str(ui.list_order_ID))
                break
    else:
        if (int(ui.order_num) <0 or int(ui.order_num)>len(InputFlag[0])-1):
            print ui.order_num
            print "Your order number is out of range"
            message = "Your order number is out of range"
            ui.textEdit.setText(message)
        elif (InputFlag[0][ui.order_num] == 1):
            print "This order already picked"
            message = "This order already picked"
            ui.textEdit.setText(message)
        else:
            for ProductID in InputFile[ui.order_num]:
                if ProductID in InputMat[:,0]:
                    if ProductID in ui.list_order_ID:
                        print "Your product is already added"
                        message = "Your product is already added"
                        ui.textEdit.setText(message)
                    else:
                        row = np.where(InputMat[:,0] == ProductID)
                        first_location=ui.rows-int(InputMat[row,2])-1
                        second_location=int(InputMat[row,1])
                        print "In our corrdinate The product x location is %d and y location is %d" %(first_location,second_location)
                        message = "Your product (x,y) location is (" + str(int(InputMat[row,1]))+","+str(int(InputMat[row,2]))+")"
                        # show the specific location of product with yellow
                        item = QtGui.QTableWidgetItem("P")
                        item.setBackground(QtCore.Qt.yellow)
                        ui.Map.setItem(first_location, second_location, item)
                        ui.textEdit.setText(message)
                        ui.valid_product = True
                        ui.list_order_ID.append(ProductID)
                        if (((first_location,second_location) in ui.list_order_loc) == 0):
                            ui.list_order_loc.append((first_location,second_location))
                        # return the location of product
                        #return(first_location,second_location)
                        ui.textEdit.setText(message)
                else:
                    ui.valid_product = False
                    print "The product you enter is not valid. Please enter a valid product Id ..."
                    message = "The product you enter is not valid. Please enter a valid product Id ..."
                    ui.textEdit.setText(message)
            InputFlag[0][ui.order_num]=1
            ui.textEdit.setText("Your order number is:%d \n" %(ui.order_num+1))
            ui.textEdit.append("Item Added: \n")
            ui.textEdit.append(str(ui.list_order_ID))

    # show message on map
