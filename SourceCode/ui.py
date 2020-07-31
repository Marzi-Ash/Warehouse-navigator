import sys
from PyQt4 import QtCore, QtGui
from Enter_Start import Enter_Start
from Enter_End import Enter_End
from Initialize_Map import Initialize_Map
from Search_ID import Search_ID, Search_ID_List
from brute_force import Brute_Force
from Show_Path import Show_Path
from modified_brute_force import Modified_Brute_Force
from Branch_Bound import Branch_Bound
from Nearest_Neighbor import Nearest_Neighbor
import os
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, rows, columns):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1100, 718)
        MainWindow.setWindowTitle('Paradiso')
        MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + "/Paradiso.png"))
        ############################################################################# Map
        self.columns = columns
        self.rows = rows
        self.list_order_loc = []
        self.list_order_ID = []
        self.previous_path = []
        self.optimal = []
        self.Dist = -1
        self.path_counter = 0
        self.counter=0
        self.backtrack = 0
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        #self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2")
        self.Map = QtGui.QTableWidget(self.centralwidget)
        self.Map.setMaximumSize(QtCore.QSize(16777215, 16777215))
        #self.Map.setGeometry(QtCore.QRect(1, 1, 633, 653))
        self.Map.setObjectName(_fromUtf8("Map"))
        self.Map.setColumnCount(self.columns)
        self.Map.setRowCount(self.rows)
        self.Map.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.Map.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        header = self.Map.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Fixed)
        header.setDefaultSectionSize(29)

        header = self.Map.verticalHeader()
        header.setResizeMode(QtGui.QHeaderView.Fixed)
        header.setDefaultSectionSize(29)
        for column in range(self.columns):
            item = QtGui.QTableWidgetItem(str(column))
            self.Map.setHorizontalHeaderItem(column, item)

        for row in range(self.rows):# It is for vertical header and white background
            item = QtGui.QTableWidgetItem(str(self.rows-row-1))
            self.Map.setVerticalHeaderItem(row, item)
            for column in range(self.columns):
                item = QtGui.QTableWidgetItem()
                item.setBackground(QtCore.Qt.white)
                self.Map.setItem(row, column, item)

        self.gridLayout_2.addWidget(self.Map, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 2)
        self.start_set_pb = QtGui.QPushButton(self.centralwidget)
        self.start_set_pb.setObjectName(_fromUtf8("start_set_pb"))
        self.gridLayout.addWidget(self.start_set_pb, 1, 10, 1, 1)
        self.order_number_radio_button = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_number_radio_button.sizePolicy().hasHeightForWidth())
        self.order_number_radio_button.setSizePolicy(sizePolicy)
        self.order_number_radio_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.order_number_radio_button.setObjectName(_fromUtf8("order_number_radio_button"))
        self.gridLayout.addWidget(self.order_number_radio_button, 0, 7, 1, 1)
        self.search_pb = QtGui.QPushButton(self.centralwidget)
        self.search_pb.setObjectName(_fromUtf8("search_pb"))
        self.gridLayout.addWidget(self.search_pb, 0, 10, 1, 1)
        self.label_start = QtGui.QLabel(self.centralwidget)
        self.label_start.setObjectName(_fromUtf8("label_start"))
        self.gridLayout.addWidget(self.label_start, 1, 0, 1, 1)
        self.Product_ID = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Product_ID.sizePolicy().hasHeightForWidth())
        self.Product_ID.setSizePolicy(sizePolicy)
        self.Product_ID.setMinimumSize(QtCore.QSize(100, 0))
        self.Product_ID.setObjectName(_fromUtf8("Product_ID"))
        self.gridLayout.addWidget(self.Product_ID, 0, 3, 1, 4)
        self.Order_number = QtGui.QLineEdit(self.centralwidget)
        self.Order_number.setMinimumSize(QtCore.QSize(50, 0))
        self.Order_number.setObjectName(_fromUtf8("Order_number"))
        self.gridLayout.addWidget(self.Order_number, 0, 8, 1, 1)
        self.reset_pb = QtGui.QPushButton(self.centralwidget)
        self.reset_pb.setObjectName(_fromUtf8("reset_pb"))
        self.gridLayout.addWidget(self.reset_pb, 3, 0, 1, 1)
        self.label_End = QtGui.QLabel(self.centralwidget)
        self.label_End.setObjectName(_fromUtf8("label_End"))
        self.gridLayout.addWidget(self.label_End, 2, 0, 1, 1)
        self.end_set_pb = QtGui.QPushButton(self.centralwidget)
        self.end_set_pb.setObjectName(_fromUtf8("end_set_pb"))
        self.gridLayout.addWidget(self.end_set_pb, 2, 10, 1, 1)
        self.label_ID = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ID.sizePolicy().hasHeightForWidth())
        self.label_ID.setSizePolicy(sizePolicy)
        self.label_ID.setObjectName(_fromUtf8("label_ID"))
        self.gridLayout.addWidget(self.label_ID, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)

        self.start_x = QtGui.QLineEdit(self.centralwidget)
        self.start_x.setObjectName(_fromUtf8("start_x"))
        self.gridLayout.addWidget(self.start_x, 1, 3, 1, 4)

        self.start_y = QtGui.QLineEdit(self.centralwidget)
        self.start_y.setObjectName(_fromUtf8("start_y"))
        self.gridLayout.addWidget(self.start_y, 1, 8, 1, 2)

        self.end_x = QtGui.QLineEdit(self.centralwidget)
        self.end_x.setObjectName(_fromUtf8("end_x"))
        self.gridLayout.addWidget(self.end_x, 2, 3, 1, 4)

        self.end_y = QtGui.QLineEdit(self.centralwidget)
        self.end_y.setObjectName(_fromUtf8("end_y"))
        self.gridLayout.addWidget(self.end_y, 2, 8, 1, 2)

        self.path_pb = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_pb.sizePolicy().hasHeightForWidth())
        self.path_pb.setSizePolicy(sizePolicy)
        self.path_pb.setObjectName(_fromUtf8("path_pb"))
        self.gridLayout.addWidget(self.path_pb, 3, 2, 1, 1)
        self.path_pb.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 7, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 2)
        self.next_order_radio_button = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_order_radio_button.sizePolicy().hasHeightForWidth())
        self.next_order_radio_button.setSizePolicy(sizePolicy)
        self.next_order_radio_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.next_order_radio_button.setObjectName(_fromUtf8("next_order_radio_button"))
        self.gridLayout.addWidget(self.next_order_radio_button, 0, 9, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 3, 1, 8)
        self.textEdit.setReadOnly(True)
        self.manually_radio_button = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manually_radio_button.sizePolicy().hasHeightForWidth())
        self.manually_radio_button.setSizePolicy(sizePolicy)
        self.manually_radio_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.manually_radio_button.setObjectName(_fromUtf8("manually_radio_button"))
        self.gridLayout.addWidget(self.manually_radio_button, 0, 1, 1, 2)
        self.back_pb = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_pb.sizePolicy().hasHeightForWidth())
        self.back_pb.setSizePolicy(sizePolicy)
        self.back_pb.setObjectName(_fromUtf8("back_pb"))
        self.gridLayout.addWidget(self.back_pb, 3, 1, 1, 1)
        self.back_pb.setMaximumSize(QtCore.QSize(150, 16777215))
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuse = QtGui.QMenu(self.menubar)
        self.menuse.setObjectName(_fromUtf8("menuse"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuse.menuAction())

        # PushButtons are assigned to their functions
        self.start_set_pb.clicked.connect(self.start_set_pb_click)
        self.end_set_pb.clicked.connect(self.end_set_pb_click)
        self.search_pb.clicked.connect(self.search_pb_click)
        self.path_pb.clicked.connect(self.path_pb_click)
        self.back_pb.clicked.connect(self.back_pb_click)
        self.Order_number.textChanged.connect(self.set_check_order)
        self.Product_ID.textChanged.connect(self.set_check_productID)



        self.retranslateUi(MainWindow)
        # All things should be reset
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.end_x.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.end_y.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_x.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Order_number.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Product_ID.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_y.clear)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.map_reset)
        QtCore.QObject.connect(self.reset_pb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.variable_reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # variables to check the validation of inputs
        self.valid_start = False
        self.valid_end = False
        self.valid_product = False
        self.Path_product = False
        self.Path_end = False
        self.path_first_time = False
        self.back_pb.setEnabled(False)

    def set_check_order (self):
        self.order_number_radio_button.setChecked(True)

    def set_check_productID (self):
        self.manually_radio_button.setChecked(True)

    def variable_reset(self):
        self.valid_start = False
        self.valid_end = False
        self.valid_product = False
        self.Path_product = False
        self.Path_end = False
        self.path_first_time = False
        self.backtrack = 0
        self.list_order_loc = []
        self.list_order_ID = []
        self.previous_path = []
        self.manually_radio_button.setChecked(False)
        self.next_order_radio_button.setChecked(False)
        self.order_number_radio_button.setChecked(False)
        self.path_pb.setEnabled(True)
        self.back_pb.setEnabled(False)
        self.search_pb.setEnabled(True)
        self.path_pb.setText(_translate("MainWindow", "Go to first item", None))

    def map_reset(self):
        self.Map.clearContents()
        Initialize_Map(self)

    def start_set_pb_click(self):
        if (self.valid_start == True):
            item = QtGui.QTableWidgetItem("")
            item.setBackground(QtCore.Qt.white)
            self.Map.setItem(self.start[0], self.start[1], item)
            if (self.valid_end == True):
                item = QtGui.QTableWidgetItem("E")
                item.setBackground(QtCore.Qt.cyan)
                self.Map.setItem(self.end[0], self.end[1], item)
        # get the start location
        x = self.start_x.text()
        y = self.start_y.text()
        if (str(x).isdigit() and str(y).isdigit()):
            self.start = (self.rows-int(y)-1,int(x))
            Enter_Start(self.rows-int(y)-1,int(x),self)
        else:
            self.textEdit.setText("Your location is not even a number ...")

    def end_set_pb_click(self):
        if (self.valid_end == True):
            item = QtGui.QTableWidgetItem("")
            item.setBackground(QtCore.Qt.white)
            self.Map.setItem(self.end[0], self.end[1], item)
            if (self.valid_start == True):
                item = QtGui.QTableWidgetItem("S")
                item.setBackground(QtCore.Qt.cyan)
                self.Map.setItem(self.start[0], self.start[1], item)
        # get the end point location
        x = self.end_x.text()
        y = self.end_y.text()
        if (str(x).isdigit() and str(y).isdigit()):
            self.end = (self.rows-int(y)-1,int(x))
            Enter_End(self.rows-int(y)-1,int(x),self)
        else:
            self.textEdit.setText("Your location is not even a number ...")

    def search_pb_click(self):

        if (self.next_order_radio_button.isChecked()):
            Search_ID_List(self,True)
        elif (self.order_number_radio_button.isChecked()):
            num = self.Order_number.text()
            if (str(num).isdigit()):
                self.order_num = int(num) -1
                Search_ID_List(self,False)
            else:
                self.textEdit.setText("Order is not even a number ...")
        elif (self.manually_radio_button.isChecked()):
            ID = self.Product_ID.text()
            if (str(ID).isdigit()):
                self.loc_product = Search_ID(int(ID), self) # search the product in database
                print self.list_order_loc
                print self.list_order_ID
                self.textEdit.append("\nItem Added: \n")
                self.textEdit.append(str(self.list_order_ID))
            else:
                self.textEdit.setText("Product ID is not even a number ...")
            ID = self.Product_ID.setText("")
        else:
            self.textEdit.setText("Please select one method to place your order ...")

    def path_pb_click(self):
        if (self.backtrack == 1):
            self.path_counter = self.path_counter + 1 # show that we need find next path
        self.backtrack = 0
        if (self.valid_end == True and self.valid_start == True and  len(self.list_order_loc) > 0):
            #clear previous_path
            for (x,y) in self.previous_path:
                # Show path on map
                item = QtGui.QTableWidgetItem("")
                item.setBackground(QtCore.Qt.white)
                self.Map.setItem(x, y, item)

            if (self.path_first_time == False):
                time_out=0
                if (len(self.list_order_loc) == 1):
                    self.Dist, self.optimal = Brute_Force(self)
                else:
                    self.Dist, self.optimal, time_out = Branch_Bound(self)
                if (time_out==1):
                    self.Dist, self.optimal = Nearest_Neighbor(self)
                    #self.Dist, self.optimal = Modified_Brute_Force(self)

                self.search_pb.setEnabled(False)
                print "optimal = %s" %self.Dist
                print "optimal = %s" %self.optimal
                self.textEdit.setText("The length of path is %s" %(self.Dist))
                # to show on map
                self.path_counter = 0
                self.previous_path = Show_Path(self.optimal[self.path_counter], self.optimal[self.path_counter+1],self)
                self.path_counter = self.path_counter+1
                self.path_first_time = True
                self.path_pb.setText(_translate("MainWindow", "Go to next Item", None))

            elif len(self.optimal)-self.path_counter >= 2:
                self.previous_path = Show_Path(self.optimal[self.path_counter], self.optimal[self.path_counter+1],self)
                self.path_counter = self.path_counter+1
                self.path_pb.setText(_translate("MainWindow", "Go to next Item", None))

            if len(self.optimal)-self.path_counter == 2:
                self.path_pb.setText(_translate("MainWindow", "Go to End", None))
            if len(self.optimal)-self.path_counter < 2:
                #self.path_pb.setText(_translate("MainWindow", "Done", None))
                self.path_pb.setText(_translate("MainWindow", "Go to End", None))
                self.path_pb.setEnabled(False)
            #Show star and end point
            item = QtGui.QTableWidgetItem("S")
            item.setBackground(QtCore.Qt.cyan)
            self.Map.setItem(self.start[0], self.start[1], item)

            item = QtGui.QTableWidgetItem("E")
            item.setBackground(QtCore.Qt.cyan)
            self.Map.setItem(self.end[0], self.end[1], item)

            if (self.start[0] == self.end[0] and self.start[1] == self.end[1]):
                item = QtGui.QTableWidgetItem("S E")
                item.setBackground(QtCore.Qt.cyan)
                self.Map.setItem(self.end[0], self.end[1], item)
        else:
            self.textEdit.setText("Please fill all the locations or product ID")

        if (self.path_counter >=2):
            self.back_pb.setEnabled(True)

    def back_pb_click(self):
        if (self.backtrack == 0):
            self.path_counter = self.path_counter - 1 # show that we need find next path
        self.backtrack = 1
        for (x,y) in self.previous_path:
            # Show path on map
            item = QtGui.QTableWidgetItem("")
            item.setBackground(QtCore.Qt.white)
            self.Map.setItem(x, y, item)
        self.path_counter = self.path_counter-1
        self.previous_path = Show_Path(self.optimal[self.path_counter], self.optimal[self.path_counter+1],self)

        item = QtGui.QTableWidgetItem("S")
        item.setBackground(QtCore.Qt.cyan)
        self.Map.setItem(self.start[0], self.start[1], item)
        item = QtGui.QTableWidgetItem("E")
        item.setBackground(QtCore.Qt.cyan)
        self.Map.setItem(self.end[0], self.end[1], item)

        if (self.start[0] == self.end[0] and self.start[1] == self.end[1]):
            item = QtGui.QTableWidgetItem("S E")
            item.setBackground(QtCore.Qt.cyan)
            self.Map.setItem(self.end[0], self.end[1], item)

        if (self.path_counter != 0):
            self.path_pb.setEnabled(True)
            self.path_pb.setText(_translate("MainWindow", "Go to next Item", None))
            if len(self.optimal)-self.path_counter == 3:
                self.path_pb.setText(_translate("MainWindow", "Go to End", None))

        if (self.path_counter <= 0):
            self.back_pb.setEnabled(False)
            self.path_pb.setEnabled(True)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Paradiso", None))
        self.path_pb.setText(_translate("MainWindow", "Go to first item", None))
        self.back_pb.setText(_translate("MainWindow", "Go back", None))
        self.reset_pb.setText(_translate("MainWindow", "Reset", None))
        self.label_ID.setText(_translate("MainWindow", "Insert profuct ID", None))
        self.label_7.setText(_translate("MainWindow", "  X", None))
        self.label_start.setText(_translate("MainWindow", "Insert Start point ", None))
        self.label_5.setText(_translate("MainWindow", "       Y", None))
        self.label_3.setText(_translate("MainWindow", "  X", None))
        self.label_End.setText(_translate("MainWindow", "Insert End Point", None))
        self.label_8.setText(_translate("MainWindow", "       Y", None))
        self.end_set_pb.setText(_translate("MainWindow", "Set", None))
        self.start_set_pb.setText(_translate("MainWindow", "Set", None))
        self.search_pb.setText(_translate("MainWindow", "Add item", None))
        self.menuse.setTitle(_translate("MainWindow", "Search", None))
        self.manually_radio_button.setText(_translate("MainWindow", "Manually", None))
        self.order_number_radio_button.setText(_translate("MainWindow", "Order Number", None))
        self.next_order_radio_button.setText(_translate("MainWindow", "Next Order", None))
