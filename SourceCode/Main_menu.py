import urllib
import smtplib
import os, sys
import string
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import *
from DataBase import *
from Initialize_Map import Initialize_Map


ReadyToLogIn = 0


class SignIn(QDialog):
    def __init__(self, parent=None):
        super(SignIn,self).__init__(parent)

        self.setWindowTitle('SignIn')
        self.username = QLineEdit(self)
        self.QUserLabel = QLabel("USERNAME")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.QPasswordLabel = QLabel("PASSWORD")

        self.btn_Submit = QPushButton("LOGIN")

        layout = QFormLayout()
        layout.addRow(self.QUserLabel,self.username)
        layout.addRow(self.QPasswordLabel,self.password)
        layout.addRow(self.btn_Submit)

        self.setLayout(layout)

        self.connect(self.btn_Submit, SIGNAL("clicked()"),self.Submit_btn)

    def Submit_btn(self):
            USERNAME = self.username.text()
            PASSWORD = self.password.text()
		
	    response = urllib.urlopen('http://m.uploadedit.com/bbtc/1559789440206.txt')
            #f = open("DataBase.txt", "r")

	    f = response.readlines()
            corrected = 0
	    
            for line in f:
		if line != '\n' and line != '\r\n':
                	l = line.strip().split('***')
			if (USERNAME == l[3]):
                    		if (PASSWORD == l[4]):
                        		corrected = 1
                    		else:
                        		corrected = 0


            if corrected == 0:
                QMessageBox.about(self, "Error", "Wrong username or password!")
                self.close()
            else:
		QMessageBox.about(self, "Signed In", "You are successfully Signed In! Use Start the Application button to run the application!")
                global ReadyToLogIn
                ReadyToLogIn = 1
                self.close()

class SignUp(QDialog):
    def __init__(self, parent=None):
        super(SignUp,self).__init__(parent)

        self.setWindowTitle('Sign Up')
        self.name = QLineEdit(self)
        self.QNameLabel = QLabel("Name")

        self.familyname = QLineEdit(self)
        self.QFamilyLabel = QLabel("Family Name")

        self.email = QLineEdit(self)
        self.QEmailLabel = QLabel("Email")

        self.username = QLineEdit(self)
        self.QUserLabel = QLabel("USERNAME")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.QPasswordLabel = QLabel("PASSWORD")

        self.passwordR = QLineEdit(self)
        self.passwordR.setEchoMode(QLineEdit.Password)
        self.QPasswordRLabel = QLabel("Repeat PASSWORD")

        self.btn_Submit = QPushButton("Sign Up")

        layout = QFormLayout()
        layout.addRow(self.QNameLabel,self.name)
        layout.addRow(self.QFamilyLabel,self.familyname)
        layout.addRow(self.QEmailLabel,self.email)
        layout.addRow(self.QUserLabel,self.username)
        layout.addRow(self.QPasswordLabel,self.password)
        layout.addRow(self.QPasswordRLabel,self.passwordR)
        layout.addRow(self.btn_Submit)

        self.setLayout(layout)

        self.connect(self.btn_Submit, SIGNAL("clicked()"),self.Submit_btn)

    def Submit_btn(self):
            NAME = self.name.text()
            FAMILY = self.familyname.text()
            EMAIL = self.email.text()
            USERNAME = self.username.text()
            PASSWORD = self.password.text()
            PASSWORDR = self.passwordR.text()

            if (NAME != '' and FAMILY != '' and EMAIL != '' and USERNAME != '' and PASSWORD != ''):
                response = urllib.urlopen('http://m.uploadedit.com/bbtc/1559789440206.txt')
                #f = open("DataBase.txt", "r")

	        f = response.readlines()

                corrected = 0
                for line in f:
		    if line != '\n' and line != '\r\n':
                    	l = line.strip().split('***')
                    	if (USERNAME == l[3]):
                            corrected = 1
                            break


                if (corrected == 1):
                    QMessageBox.about(self, "Error", "Username already exists!")
                    self.close()
                elif (PASSWORD == PASSWORDR):
                    # creates SMTP session 
		    s = smtplib.SMTP('smtp.gmail.com', 587) 
                    # start TLS for security 
                    s.starttls() 
                    # Authentication
                    s.login("paradisoapp2019@gmail.com", "Amir123456!")
                    # message to be sent  
		    SUBJECT = "New Request for Registration!"
		    BODY = str('FirstName = '+NAME+'\n'+'Family name = '+FAMILY+'\n'+'Email = '+EMAIL+'\n'+'Username = '+USERNAME+'\n'+'Password = '+PASSWORD+'\n')
		    message = string.join(("SUBJECT: %s" % SUBJECT,BODY), "\r\n")

                    # sending the mail 
                    s.sendmail("paradisoapp2019@gmail.com", "paradisoapp2019@gmail.com", message)
                    # terminating the session 
                    s.quit()

                    QMessageBox.about(self, "Congratulations!", "Your request for Sign Up to the application has been sent to us! After at last 24 hours, your registration will be confirmed or denied!")
                    self.close()
                else:
                    QMessageBox.about(self, "Error", "Password fields are not match!")
                    self.close()
            else:
                QMessageBox.about(self, "Error", "Please complete all the fields!")
                self.close()


class MainMenu(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        self.setGeometry(800, 300, 400, 350)
        self.setWindowTitle('Welcome to Paradiso')
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + "/Paradiso.png"))

        picture = QtGui.QLabel(self)
        picture.setPixmap(QtGui.QPixmap(os.getcwd() + "/Paradiso_logo.png"))
        grid.addWidget(picture)



        button = QtGui.QPushButton("Start the Application")
        grid.addWidget(button)
        button.clicked.connect(self.StartTheApp)

        button = QtGui.QPushButton("Sign In")
        grid.addWidget(button)
        button.clicked.connect(self.SignInButton)

        button = QtGui.QPushButton("Sign Up")
        grid.addWidget(button)
        button.clicked.connect(self.SignUpButton)

        button = QtGui.QPushButton("Sign Out")
        grid.addWidget(button)
        button.clicked.connect(self.SignOutButton)

        button = QtGui.QPushButton("Help")
        grid.addWidget(button)
        button.clicked.connect(self.HelpButton)

        button = QtGui.QPushButton("Exit")
        grid.addWidget(button)
        button.clicked.connect(self.closeButton)

    def SignOutButton(self):
        global ReadyToLogIn
        if (ReadyToLogIn == 0):
            QMessageBox.about(self, "Error", "You are not Signed In!")
        else:
            ReadyToLogIn = 0
            QMessageBox.about(self, "Error", "You are successuflly Signed Out!")

    def StartTheApp(self):
        if (ReadyToLogIn == 0):
            QMessageBox.about(self, "Error", "You are not Signed In! Use Sign In option to Sign In first.")
        else:
             #run app
             self.window = QtGui.QMainWindow()
             self.ui= Ui_MainWindow()
             self.ui.setupUi(self.window, LocMat.shape[0], LocMat.shape[1])
             Initialize_Map(self.ui) # show shelves on map
             self.window.show()
             self.hide()

    def SignInButton(self):
        if (ReadyToLogIn == 0):
            self.nd = SignIn(self)
            self.nd.show()
        else:
            QMessageBox.about(self, "Error", "You are already Signed In, use Start the Application button to run the application!")

    def SignUpButton(self):
        self.nd = SignUp(self)
        self.nd.show()

    def HelpButton(self):
        QMessageBox.about(self, "Help", "This is the Paradiso Application!\n\nIf you are already a user, use Sign In option to login.\nOtherwise, use the Sign Up option to become a member.\n\nThank you! :)")

    def closeButton(self):
        self.close()
