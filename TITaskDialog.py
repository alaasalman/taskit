""" 
    Copyright 2007 Alaa Salman <alaa@codedemigod.com>
    
    This file is part of TaskIt.

    TaskIt is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    TaskIt is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from ui import TaskInputDialog

class TITaskDialog(QtGui.QDialog):
    def __init__(self, p_Parent = None):
        QtGui.QDialog.__init__(self, p_Parent)
        
        self.ui = TaskInputDialog.Ui_Dialog()
        self.ui.setupUi(self)
        
    def taskText(self):
        return self.ui.taskTextEdit.toPlainText()
        
    def categoryText(self):
        return self.ui.categoryLineEdit.text()
        
    def setTaskText(self, newTaskText):
        self.ui.taskTextEdit.setText(newTaskText)
        
    def setCategoryText(self, newCategoryText):
        self.ui.categoryLineEdit.setText(newCategoryText)
        
    def setReadOnlyMode(self):
        self.ui.taskTextEdit.setEnabled(False)
        
