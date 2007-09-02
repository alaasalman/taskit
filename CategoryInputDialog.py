# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CategoryInputDialog.ui'
#
# Created: Sat Sep  1 08:42:41 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,392,119).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowIcon(QtGui.QIcon("IconResources/book.png"))

        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10,20,371,35))
        self.layoutWidget.setObjectName("layoutWidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setMargin(2)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.categoryLabel = QtGui.QLabel(self.layoutWidget)
        self.categoryLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.categoryLabel.setObjectName("categoryLabel")
        self.hboxlayout.addWidget(self.categoryLabel)

        self.categoryLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.hboxlayout.addWidget(self.categoryLineEdit)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50,70,331,32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add New Category", None, QtGui.QApplication.UnicodeUTF8))
        self.categoryLabel.setText(QtGui.QApplication.translate("Dialog", "Category", None, QtGui.QApplication.UnicodeUTF8))

