import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from MainForm import Ui_MainWindow
from GTDCategoryInput import GTDCategoryInput
from GTDTaskInput import GTDTaskInput
from GTDAbout import GTDAbout
from DBHandler import DBHandler
from GTDCategoryWidget import GTDCategoryWidget
from GTDTaskWidget import GTDTaskWidget


textColumnIndex = 0
idColumnIndex = 1

class GTDWindow(QtGui.QMainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        headerLabels = QtCore.QStringList()
        
        headerLabels += "Task List"
        headerLabels += "ID"
        
        self.ui.treeWidget.setHeaderLabels(headerLabels)
        self.ui.treeWidget.hideColumn(idColumnIndex)
        self.ui.treeWidget.expandAll()
        
        self.dbHandler = DBHandler()
        self.doConnections()
        
    def doConnections(self):
        self.connect(self.ui.actionAddTask, QtCore.SIGNAL("triggered()"), self.addTask)
        self.connect(self.ui.actionRemoveTask, QtCore.SIGNAL("triggered()"), self.removeTask)
        self.connect(self.ui.actionAddCategory, QtCore.SIGNAL("triggered()"), self.addCategory)
        self.connect(self.ui.actionRemoveCategory, QtCore.SIGNAL("triggered()"), self.removeCategory)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.displayAbout)
        self.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveDB)
        self.connect(self.ui.actionLoad, QtCore.SIGNAL("triggered()"), self.loadDB)
        self.connect(self.ui.actionClear, QtCore.SIGNAL("triggered()"), self.clearWindow)
        

    def addTask(self):
        #this is not necessarily a category, can be a task and the user
        #is adding subtasks
        selectedItem = self.ui.treeWidget.currentItem()
        
        if(selectedItem != None):
            
            #for now, we don't allow tasks to have subtasks
            if(isinstance(selectedItem, GTDTaskWidget)):
                return
                
            gtdTaskInput = GTDTaskInput()
            
            selectedCategoryText = selectedItem.text(textColumnIndex)
            gtdTaskInput.setCategoryText(selectedCategoryText)
            
            gtdTaskInput.exec_()
            
            if(gtdTaskInput.result() == GTDTaskInput.Accepted):
                taskText = gtdTaskInput.taskText()
                
                taskWidget = GTDTaskWidget(taskText)
            
                selectedItem.addChild(taskWidget)
                self.ui.treeWidget.expandItem(selectedItem)
        
    def removeTask(self):
        #this could be a task or a subtask
        selectedItem = self.ui.treeWidget.currentItem()
        
        if(selectedItem != None):
            selectedItemParent = selectedItem.parent()
            
            if(selectedItemParent != None):
                selectedTaskIndex = self.ui.treeWidget.currentIndex().row()
                selectedItemParent.takeChild(selectedTaskIndex)
        
        
    def addCategory(self):
        gtdInput = GTDCategoryInput()
        gtdInput.exec_()
        
        if(gtdInput.result() == GTDCategoryInput.Accepted):
            categoryText = gtdInput.categoryText()
                        
            categoryWidget = GTDCategoryWidget(categoryText)
            
            self.ui.treeWidget.addTopLevelItem(categoryWidget)
            self.ui.treeWidget.expandItem(categoryWidget)
        
    def removeCategory(self):
        selectedCategoryIndex = self.ui.treeWidget.currentIndex().row()
        self.ui.treeWidget.takeTopLevelItem(selectedCategoryIndex)
        
    def displayAbout(self):
        gtdAbout = GTDAbout()
        gtdAbout.exec_()
        
    def saveDB(self):
        treeModel = self.ui.treeWidget.model()
        dbHandler = self.dbHandler
        
        dbHandler.deleteAllCategories()
        
        for rowNumber in range(treeModel.rowCount()):
            currentModelTextIndex = treeModel.index(rowNumber, textColumnIndex)
            currentModelIdIndex = treeModel.index(rowNumber, idColumnIndex)
            
            categoryText = str(treeModel.data(currentModelTextIndex).toString())
            
            category_id = dbHandler.addCategory(categoryText)
            treeModel.setData(currentModelIdIndex, QtCore.QVariant(category_id))
            
            if(treeModel.hasChildren(currentModelTextIndex) == True):
                for childRowNumber in range(treeModel.rowCount(currentModelTextIndex)):
                    childModelTextIndex = currentModelTextIndex.child(childRowNumber, textColumnIndex)
                    childModelIdIndex = currentModelIdIndex.child(childRowNumber, idColumnIndex)
                    
                    taskText = str(childModelTextIndex.data().toString())
                    
                    childModel = childModelTextIndex.model()
                    
                    task_id = dbHandler.addTask(taskText, category_id)
                    childModel.setData(childModelIdIndex, QtCore.QVariant(task_id))
                    
        
        
    def loadDB(self):
        
        self.ui.treeWidget.clear()
        
        dbHandler = self.dbHandler
        categories = dbHandler.getAllCategories()
        
        for cat in categories:
            tasksByCategory = dbHandler.getTasksByCategory(cat)
            
            categoryWidget = GTDCategoryWidget(cat.categorytitle, cat.id)
            
            if(tasksByCategory != None):
                for task in tasksByCategory:
                    taskWidget = GTDTaskWidget(task.tasktext, task.id)
                    categoryWidget.addChild(taskWidget)
            
            self.ui.treeWidget.addTopLevelItem(categoryWidget)
            self.ui.treeWidget.expandItem(categoryWidget)
            
            
    def clearWindow(self):
        self.ui.treeWidget.clear()
            
            
            
