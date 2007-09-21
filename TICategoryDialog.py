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

from ui import CategoryInputDialog

class TICategoryDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        self.ui = CategoryInputDialog.Ui_Dialog()
        self.ui.setupUi(self)
        
    def categoryText(self):
        return self.ui.categoryLineEdit.text()
        
    def setCategoryText(self, newCategoryText):
        self.ui.categoryLineEdit.setText(newCategoryText)
        
