# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created: Sat Sep 15 17:51:25 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,682,602).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0,0,681,511))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0,0,682,25))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuOperations = QtGui.QMenu(self.menuBar)
        self.menuOperations.setObjectName("menuOperations")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(self.toolBar)

        self.actionAddTask = QtGui.QAction(MainWindow)
        self.actionAddTask.setIcon(QtGui.QIcon("IconResources/script_add.png"))
        self.actionAddTask.setObjectName("actionAddTask")

        self.actionRemoveTask = QtGui.QAction(MainWindow)
        self.actionRemoveTask.setIcon(QtGui.QIcon("IconResources/script_delete.png"))
        self.actionRemoveTask.setObjectName("actionRemoveTask")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setIcon(QtGui.QIcon("IconResources/door_in.png"))
        self.actionExit.setObjectName("actionExit")

        self.actionAddCategory = QtGui.QAction(MainWindow)
        self.actionAddCategory.setIcon(QtGui.QIcon("IconResources/book_add.png"))
        self.actionAddCategory.setObjectName("actionAddCategory")

        self.actionRemoveCategory = QtGui.QAction(MainWindow)
        self.actionRemoveCategory.setIcon(QtGui.QIcon("IconResources/book_delete.png"))
        self.actionRemoveCategory.setObjectName("actionRemoveCategory")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(QtGui.QIcon("IconResources/anchor.png"))
        self.actionAbout.setObjectName("actionAbout")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setIcon(QtGui.QIcon("IconResources/disk.png"))
        self.actionSave.setObjectName("actionSave")

        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setIcon(QtGui.QIcon("IconResources/folder_go.png"))
        self.actionLoad.setObjectName("actionLoad")

        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setIcon(QtGui.QIcon("IconResources/bin_empty.png"))
        self.actionClear.setObjectName("actionClear")

        self.actionEditTask = QtGui.QAction(MainWindow)
        self.actionEditTask.setIcon(QtGui.QIcon("IconResources/script_edit.png"))
        self.actionEditTask.setObjectName("actionEditTask")

        self.actionEditCategory = QtGui.QAction(MainWindow)
        self.actionEditCategory.setIcon(QtGui.QIcon("IconResources/book_edit.png"))
        self.actionEditCategory.setObjectName("actionEditCategory")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuOperations.addAction(self.actionAddCategory)
        self.menuOperations.addAction(self.actionEditCategory)
        self.menuOperations.addAction(self.actionRemoveCategory)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.actionAddTask)
        self.menuOperations.addAction(self.actionEditTask)
        self.menuOperations.addAction(self.actionRemoveTask)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.actionClear)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOperations.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddTask)
        self.toolBar.addAction(self.actionRemoveTask)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddCategory)
        self.toolBar.addAction(self.actionRemoveCategory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEditCategory)
        self.toolBar.addAction(self.actionEditTask)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit,QtCore.SIGNAL("triggered()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TaskIt", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1,QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOperations.setTitle(QtGui.QApplication.translate("MainWindow", "Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddTask.setText(QtGui.QApplication.translate("MainWindow", "New Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveTask.setText(QtGui.QApplication.translate("MainWindow", "Remove Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddCategory.setText(QtGui.QApplication.translate("MainWindow", "New Category", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveCategory.setText(QtGui.QApplication.translate("MainWindow", "Remove Category", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditTask.setText(QtGui.QApplication.translate("MainWindow", "Edit Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditCategory.setText(QtGui.QApplication.translate("MainWindow", "Edit Category", None, QtGui.QApplication.UnicodeUTF8))

