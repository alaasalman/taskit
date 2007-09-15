# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutDialog.ui'
#
# Created: Sat Sep 15 18:29:55 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,400,270).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowIcon(QtGui.QIcon("IconResources/anchor.png"))
        Dialog.setModal(True)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setWindowModality(QtCore.Qt.WindowModal)
        self.buttonBox.setGeometry(QtCore.QRect(50,230,341,32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(5,5,390,220))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")

        self.authorTab = QtGui.QWidget()
        self.authorTab.setObjectName("authorTab")

        self.authorTextBrowser = QtGui.QTextBrowser(self.authorTab)
        self.authorTextBrowser.setGeometry(QtCore.QRect(5,5,380,180))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorTextBrowser.sizePolicy().hasHeightForWidth())
        self.authorTextBrowser.setSizePolicy(sizePolicy)
        self.authorTextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.authorTextBrowser.setObjectName("authorTextBrowser")
        self.tabWidget.addTab(self.authorTab,"")

        self.licenseTab = QtGui.QWidget()
        self.licenseTab.setObjectName("licenseTab")

        self.licenseTextBrowser = QtGui.QTextBrowser(self.licenseTab)
        self.licenseTextBrowser.setGeometry(QtCore.QRect(5,5,380,180))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.licenseTextBrowser.sizePolicy().hasHeightForWidth())
        self.licenseTextBrowser.setSizePolicy(sizePolicy)
        self.licenseTextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.licenseTextBrowser.setObjectName("licenseTextBrowser")
        self.tabWidget.addTab(self.licenseTab,"")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.authorTab), QtGui.QApplication.translate("Dialog", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.licenseTab), QtGui.QApplication.translate("Dialog", "License", None, QtGui.QApplication.UnicodeUTF8))

