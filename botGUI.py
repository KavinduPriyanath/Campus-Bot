from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5.QtGui import *
import sys
from assignment import *
import vleaa

def screen():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setWindowIcon(QIcon('Player.png'))
	win.setGeometry(400,200,350,300)
	win.setWindowTitle("UCSC Bot")
	win.setStyleSheet("background-image: url(bg.jpg);")

	label1 = QtWidgets.QLabel(win)
	label1.setText("Just One Click")
	label1.setFont(QFont('Courier', 30))
	label1.setGeometry(90,35, 220, 20)
	label1.setStyleSheet("font-weight: bold;")

	button1 = QtWidgets.QPushButton(win)
	button1.setText("Assignments")
	button1.clicked.connect(showPop)
	button1.setGeometry(182, 110, 135, 40)
	button1.setStyleSheet(
							"QPushButton" 
							"{" 
							"background-color: yellow;" 
							"}" 
							"QPushButton::hover" 
							"{" 
							"background-color: blue; font-weight: bold;" 
							"}" 
							"QPushButton::pressed" 
							"{" 
							"background-color: red; font-weight: bold;" 
							"}")
	button1.setFont(QFont('SansSerif', 15))
	button1.setToolTip("Check out the Upcoming Assignments")

	button2 = QtWidgets.QPushButton(win)
	button2.setText("Wander")
	button2.clicked.connect(wander)
	button2.setGeometry(190, 170, 120, 40)
	button2.setStyleSheet(
							"QPushButton" 
							"{" 
							"background-color: yellow;" 
							"}" 
							"QPushButton::hover" 
							"{" 
							"background-color: blue; font-weight: bold;" 
							"}" 
							"QPushButton::pressed" 
							"{" 
							"background-color: red; font-weight: bold;" 
							"}")
	button2.setFont(QFont('SansSerif', 15))
	button2.setToolTip("Activate bot to pretend them that you are active in the site")

	image1 = QPixmap('Player.png')
	image2 = image1.scaled(100, 126)
	label2 = QtWidgets.QLabel(win)
	label2.setPixmap(image2)
	label2.setGeometry(0, 105, 100, 126)

	win.show()
	sys.exit(app.exec_())

def showPop():
	msg = QDialog()
	msg.setWindowTitle("Upcoming Assignments")
	msg.setGeometry(200,200,670,500)
	msg.setWindowIcon(QIcon('Player.png'))
	text1 = QtWidgets.QLabel(msg)
	text1.setText(upevent.text)
	text1.setFont(QFont('SansSerif', 10))
	msg.show()
	x = msg.exec_()

def buttonpress():
	perform()

def wander():
	vleaa.execute()

screen()