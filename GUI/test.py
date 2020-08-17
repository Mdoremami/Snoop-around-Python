# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def font_maker(self):
		# Font Selection
		self.labelfont = QtGui.QFont()
		self.labelfont.setFamily("Times New Roman")
		self.labelfont.setPointSize(24)
		self.labelfont.setBold(True)
		self.labelfont.setItalic(True)
		self.labelfont.setWeight(75)
		
		self.buttfont = QtGui.QFont()
		self.buttfont.setFamily("Times New Roman")
		self.buttfont.setPointSize(13)
		self.buttfont.setBold(False)
		self.buttfont.setItalic(False)
		self.buttfont.setWeight(75)
	def setupUi(self, MainWindow):
		self.font_maker()
		font = self.labelfont
		buttfont = self.buttfont
		# Main Window
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(500, 500)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		# Button 1
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(80, 190, 100, 100))
		self.pushButton.setFont(buttfont)
		self.pushButton.setObjectName('pushButton')
		#Label 1
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(70, 50, 231, 71))
		self.label.setFont(font)
		self.label.setObjectName("label")
		# Menubar
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuEdit = QtWidgets.QMenu(self.menubar)
		self.menuEdit.setObjectName("menuEdit")
		MainWindow.setMenuBar(self.menubar)
		# Statusbar
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		# Submenues
		self.actionNew = QtWidgets.QAction(MainWindow)
		self.actionNew.setObjectName("actionNew")
		self.actionSave = QtWidgets.QAction(MainWindow)
		self.actionSave.setObjectName("actionSave")
		self.actionCopy = QtWidgets.QAction(MainWindow)
		self.actionCopy.setObjectName("actionCopy")
		self.actionPaste = QtWidgets.QAction(MainWindow)
		self.actionPaste.setObjectName("actionPaste")
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionSave)
		self.menuEdit.addAction(self.actionCopy)
		self.menuEdit.addAction(self.actionPaste)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuEdit.menuAction())
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Press Me Honey :x"))
		self.pushButton.adjustSize()
		self.label.setText(_translate("MainWindow", "Greetings Babe"))
		self.label.adjustSize()
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
		self.actionNew.setText(_translate("MainWindow", "New"))
		self.actionNew.setStatusTip(_translate("MainWindow", "Creates a new file"))
		self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
		self.actionSave.setText(_translate("MainWindow", "Save"))
		self.actionSave.setStatusTip(_translate("MainWindow", "Saves the file"))
		self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
		self.actionCopy.setText(_translate("MainWindow", "Copy"))
		self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
		self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
		self.actionPaste.setText(_translate("MainWindow", "Paste"))
		self.actionPaste.setStatusTip(_translate("MainWindow", "Paste"))
		self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

