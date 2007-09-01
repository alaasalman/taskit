import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from TaskInputDialog import Ui_Dialog

class GTDTaskInput(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
    def taskText(self):
        return self.ui.taskLineEdit.text()
        
    def categoryText(self):
        return self.ui.categoryLineEdit.text()
        
    def setTaskText(self, newTaskText):
        self.ui.taskLineEdit.setText(newTaskText)
        
    def setCategoryText(self, newCategoryText):
        self.ui.categoryLineEdit.setText(newCategoryText)
        
