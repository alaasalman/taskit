import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from CategoryInputDialog import Ui_Dialog

class GTDCategoryInput(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
    def categoryText(self):
        return self.ui.categoryLineEdit.text()
        
    def setCategoryText(self, newCategoryText):
        self.ui.categoryLineEdit.setText(newCategoryText)
        
