# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskInputDialog.ui'
#
# Created: Sat Sep 15 17:51:25 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,392,164).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowIcon(QtGui.QIcon("IconResources/script.png"))

        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10,24,371,66))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.taskLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.gridlayout.addWidget(self.taskLineEdit,1,1,1,1)

        self.categoryLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.categoryLineEdit.setEnabled(False)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.gridlayout.addWidget(self.categoryLineEdit,0,1,1,1)

        self.taskLabel = QtGui.QLabel(self.layoutWidget)
        self.taskLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.taskLabel.setObjectName("taskLabel")
        self.gridlayout.addWidget(self.taskLabel,1,0,1,1)

        self.categoryLabel = QtGui.QLabel(self.layoutWidget)
        self.categoryLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.categoryLabel.setObjectName("categoryLabel")
        self.gridlayout.addWidget(self.categoryLabel,0,0,1,1)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50,117,331,32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add New Task", None, QtGui.QApplication.UnicodeUTF8))
        self.taskLabel.setText(QtGui.QApplication.translate("Dialog", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.categoryLabel.setText(QtGui.QApplication.translate("Dialog", "Category", None, QtGui.QApplication.UnicodeUTF8))

