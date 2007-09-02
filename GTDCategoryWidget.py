from PyQt4 import QtCore
from PyQt4 import QtGui

textColumnIndex = 0
idColumnIndex = 1

class GTDCategoryWidget(QtGui.QTreeWidgetItem):
    
    def __init__(self, p_CategoryText="", p_CategoryId=0):
        QtGui.QTreeWidgetItem.__init__(self)
        
        categoryIcon = QtGui.QIcon("IconResources/book.png")
        
        self.setText(textColumnIndex, p_CategoryText)
        self.setText(idColumnIndex, str(p_CategoryId))
            
        self.setIcon(textColumnIndex, categoryIcon)
        
    def categoryId(self):
        return self.text(idColumnIndex)
        
    def categoryText(self):
        return self.text(textColumnIndex)
    
    def setCategoryText(self, p_CategoryText):
        self.setText(textColumnIndex, p_CategoryText)

