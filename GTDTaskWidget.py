from PyQt4 import QtCore
from PyQt4 import QtGui

textColumnIndex = 0
idColumnIndex = 1

class GTDTaskWidget(QtGui.QTreeWidgetItem):
       
    def __init__(self, p_TaskText="", p_TaskId=0):
        
        QtGui.QTreeWidgetItem.__init__(self)
        
        taskIcon = QtGui.QIcon("IconResources/script.png")
                
        self.setText(textColumnIndex, p_TaskText)
        self.setText(idColumnIndex, str(p_TaskId))
                
        self.setIcon(textColumnIndex, taskIcon)
        
    def taskCategoryId(self):
        taskCategory = self.parent()
        return taskCategory.text(idColumnIndex)
        
    def taskCategoryText(self):
        taskCategory = self.parent()
        return taskCategory.text(textColumnIndex)
        
    def taskId(self):
        return self.text(idColumnIndex)
        
    def taskText(self):
        return self.text(textColumnIndex)
        
    def setTaskText(self, p_TaskText):
        self.setText(textColumnIndex, p_TaskText)
