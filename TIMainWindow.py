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

from ui import MainWindow
from TICategoryDialog import TICategoryDialog
from TITaskDialog import TITaskDialog
from TIAboutDialog import TIAboutDialog

from TICategoryWidget import TICategoryWidget
from TITaskWidget import TITaskWidget

from DBHandler import DBHandler

textColumnIndex = 0
idColumnIndex = 1

class TIMainWindow(QtGui.QMainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.modified = False
        self.title = self.windowTitle()
        
        headerLabels = QtCore.QStringList()
        
        headerLabels += "Task List"
        headerLabels += "ID"
        
        self.ui.treeWidget.setHeaderLabels(headerLabels)
        self.ui.treeWidget.hideColumn(idColumnIndex)
        self.ui.treeWidget.expandAll()
        
        self.dbHandler = DBHandler()
        self.doConnections()
        self.setActionIcons()
        
    def doConnections(self):
        self.connect(self.ui.actionAddTask, QtCore.SIGNAL("triggered()"), self.addTask)
        self.connect(self.ui.actionRemoveTask, QtCore.SIGNAL("triggered()"), self.removeTask)
        self.connect(self.ui.actionAddCategory, QtCore.SIGNAL("triggered()"), self.addCategory)
        self.connect(self.ui.actionRemoveCategory, QtCore.SIGNAL("triggered()"), self.removeCategory)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.displayAbout)
        self.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveDB)
        self.connect(self.ui.actionLoad, QtCore.SIGNAL("triggered()"), self.loadDB)
        self.connect(self.ui.actionClear, QtCore.SIGNAL("triggered()"), self.clearWindow)
        self.connect(self.ui.actionEditTask, QtCore.SIGNAL("triggered()"), self.editTask)
        self.connect(self.ui.actionEditCategory, QtCore.SIGNAL("triggered()"), self.editCategory)
        self.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.exit)
        
    def setActionIcons(self):
        self.ui.actionAddTask.setIcon(QtGui.QIcon("IconResources/script_add.png"))
        self.ui.actionRemoveTask.setIcon(QtGui.QIcon("IconResources/script_delete.png"))
        self.ui.actionExit.setIcon(QtGui.QIcon("IconResources/door_in.png"))
        self.ui.actionAddCategory.setIcon(QtGui.QIcon("IconResources/book_add.png"))
        self.ui.actionRemoveCategory.setIcon(QtGui.QIcon("IconResources/book_delete.png"))
        self.ui.actionAbout.setIcon(QtGui.QIcon("IconResources/anchor.png"))
        self.ui.actionSave.setIcon(QtGui.QIcon("IconResources/disk.png"))
        self.ui.actionLoad.setIcon(QtGui.QIcon("IconResources/folder_go.png"))
        self.ui.actionClear.setIcon(QtGui.QIcon("IconResources/bin_empty.png"))
        self.ui.actionEditTask.setIcon(QtGui.QIcon("IconResources/script_edit.png"))
        self.ui.actionEditCategory.setIcon(QtGui.QIcon("IconResources/book_edit.png"))
        

    def addTask(self):
        #this is not necessarily a category, can be a task and the user
        #is adding subtasks
        selectedItem = self.ui.treeWidget.currentItem()
        
        if(selectedItem != None):
            
            #for now, we don't allow tasks to have subtasks
            if(isinstance(selectedItem, TITaskWidget)):
                return
                
            taskDialog = TITaskDialog()
            
            selectedCategoryText = selectedItem.text(textColumnIndex)
            taskDialog.setCategoryText(selectedCategoryText)
            
            taskDialog.exec_()
            
            if(taskDialog.result() == TITaskDialog.Accepted):
                taskText = taskDialog.taskText()
                
                taskWidget = TITaskWidget(taskText)
            
                selectedItem.addChild(taskWidget)
                self.ui.treeWidget.expandItem(selectedItem)
                self.tasklistModification(True)
        
    def removeTask(self):
        #this could be a task or a subtask
        selectedItem = self.ui.treeWidget.currentItem()
        
        if(selectedItem != None):
            selectedItemParent = selectedItem.parent()
            
            if(selectedItemParent != None):
                selectedTaskIndex = self.ui.treeWidget.currentIndex().row()
                selectedItemParent.takeChild(selectedTaskIndex)
                self.tasklistModification(True)
        
        
    def addCategory(self):
        categoryDialog = TICategoryDialog()
        categoryDialog.exec_()
        
        if(categoryDialog.result() == TICategoryDialog.Accepted):
            categoryText = categoryDialog.categoryText()
                        
            categoryWidget = TICategoryWidget(categoryText)
            
            self.ui.treeWidget.addTopLevelItem(categoryWidget)
            self.ui.treeWidget.expandItem(categoryWidget)
            self.tasklistModification(True)
        
    def removeCategory(self):
        selectedCategoryIndex = self.ui.treeWidget.currentIndex().row()
        self.ui.treeWidget.takeTopLevelItem(selectedCategoryIndex)
        self.tasklistModification(True)
        
    def displayAbout(self):
        aboutDialog = TIAboutDialog()
        aboutDialog.exec_()
        
    def saveDB(self):
        if(self.isModified() == True):
            buttonChoice = QtGui.QMessageBox.warning(self, self.title, "Are you sure you want to overwrite?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if(buttonChoice == QtGui.QMessageBox.No):
                return
        else: # no modifications, don't do any work
            return
                
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
            
            self.tasklistModification(False)        
        
        
    def loadDB(self):
        if(self.isModified() == True):
            buttonChoice = QtGui.QMessageBox.warning(self, self.title, "You have unsaved modifications, are you sure you want to overwrite?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if(buttonChoice == QtGui.QMessageBox.No):
                return
                                                            
        self.ui.treeWidget.clear()
        
        dbHandler = self.dbHandler
        categories = dbHandler.getAllCategories()
        
        for cat in categories:
            tasksByCategory = dbHandler.getTasksByCategory(cat)
            
            categoryWidget = TICategoryWidget(cat.categorytitle, cat.id)
            
            if(tasksByCategory != None):
                for task in tasksByCategory:
                    taskWidget = TITaskWidget(task.tasktext, task.id)
                    categoryWidget.addChild(taskWidget)
            
            self.ui.treeWidget.addTopLevelItem(categoryWidget)
            self.ui.treeWidget.expandItem(categoryWidget)
            self.tasklistModification(False)
            
            
    def clearWindow(self):
        self.ui.treeWidget.clear()
        self.tasklistModification(True)
        
    def editCategory(self):
        selectedCategory = self.ui.treeWidget.currentItem()
        
        if(selectedCategory != None):
            
            #just edit categories
            if(not isinstance(selectedCategory, TICategoryWidget)):
                return
            
            selectedCategoryText = selectedCategory.categoryText()
                        
            categoryInput = TICategoryDialog()
            categoryInput.setCategoryText(selectedCategoryText)
            categoryInput.exec_()
            
            if(categoryInput.result() == TICategoryDialog.Accepted):
                #this returns QString so str() it
                selectedCategoryId = str(selectedCategory.categoryId())
                updatedCategoryText = str(categoryInput.categoryText())
                
                #dbHandler = self.dbHandler
                
                #dbHandler.editCategory(selectedCategoryId, updatedCategoryText)
                
                selectedCategory.setCategoryText(updatedCategoryText)
                self.tasklistModification(True)
        
        
    def editTask(self):
        selectedTask = self.ui.treeWidget.currentItem()
        
        if(selectedTask != None):
            
            if(not isinstance(selectedTask, TITaskWidget)):
                return
                
            selectedTaskText = selectedTask.taskText()
            
            taskInput = TITaskDialog()
            taskInput.setCategoryText(selectedTask.taskCategoryText())
            taskInput.setTaskText(selectedTaskText)
            taskInput.exec_()
            
            if(taskInput.result() == TITaskDialog.Accepted):
                selectedTaskId = str(selectedTask.taskId())
                updatedTaskText = str(taskInput.taskText())
                
                #dbHandler = self.dbHandler
                #dbHandler.editTask(selectedTaskId, updatedTaskText)
                
                selectedTask.setTaskText(updatedTaskText)
                self.tasklistModification(True)
    
    #return status of modification
    #TODO modified() seems to confuse python because it shares a name with an instance variable
    def isModified(self):
        return self.modified
    
    def setModified(self, p_ModifiedStatus):
        self.modified = p_ModifiedStatus
            
    def tasklistModification(self, p_ModificationStatus):
        
        #we're not in modification state
        if(self.isModified() == False):
            if(p_ModificationStatus == True):
                self.setModified(True)
                self.setWindowTitle(self.title + "*")
            else:
                return
        else: #previous modification
            if(p_ModificationStatus == False):
                self.setModified(False)
                self.setWindowTitle(self.title)
            else:
                return
                
    def exit(self):
        if(self.isModified() == True):
            buttonChoice = QtGui.QMessageBox.warning(self, self.title, "You have unsaved modifications, are you sure you want to quit?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                                                        
            if(buttonChoice == QtGui.QMessageBox.Yes):
                self.close()
            else:
                return
        else:
            self.close()
            
