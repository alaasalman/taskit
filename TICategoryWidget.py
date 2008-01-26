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

from PyQt4 import QtCore
from PyQt4 import QtGui

textColumnIndex = 0
idColumnIndex = 1

class TICategoryWidget(QtGui.QTreeWidgetItem):
    
    def __init__(self, p_CategoryText="", p_CategoryId=0):
        QtGui.QTreeWidgetItem.__init__(self)
        
        categoryIcon = QtGui.QIcon("IconResources/book.png")
        
        self.setText(textColumnIndex, p_CategoryText)
        self.setText(idColumnIndex, str(p_CategoryId))
            
        self.setIcon(textColumnIndex, categoryIcon)
        
    def categoryId(self):
        return str(self.text(idColumnIndex))
        
    def categoryText(self):
        return str(self.text(textColumnIndex))
    
    def setCategoryText(self, p_CategoryText):
        self.setText(textColumnIndex, p_CategoryText)

