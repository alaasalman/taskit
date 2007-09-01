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
