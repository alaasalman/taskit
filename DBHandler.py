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
 
from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm import relation

from model.Task import Task
from model.Category import Category

class DBHandler():
    def __init__(self):
        engine = create_engine("sqlite:///db/tasklist.db", echo=True)
        self.metadata = MetaData()

        tasks_table = Table("tasks", self.metadata,
            Column("id", Integer, primary_key=True),
            Column("tasktext", String),
            Column("category_id", Integer, ForeignKey("categories.id"))
        )
        
        categories_table = Table("categories", self.metadata,
            Column("id", Integer, primary_key=True),
            Column("categorytitle", String)
        )

        self.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine, autoflush=True, transactional=True)
        
        mapper(Category, categories_table, properties={
            "tasks":relation(Task, backref="category")
            })
        
        mapper(Task, tasks_table)
        
        
    
    def addTask(self, p_TaskText, p_CategoryId):
        task = Task(p_TaskText, p_CategoryId)
        
        session = self.session()
        session.save(task)
        session.commit()
        
        return task.id
        

    def addCategory(self, p_CategoryTitle):
        category = Category(p_CategoryTitle)
        
        session = self.session()
        session.save(category)
        session.commit()
        
        return category.id
        
    def editCategory(self, p_CategoryId, p_CategoryText):
        session = self.session()
        
        #this is probably not needed for an update...see SA docs again
        query = session.query(Category).filter(Category.id==p_CategoryId)
        
        cat = query.first()
        cat.categorytitle = p_CategoryText
        
        session.update(cat)
        session.commit()
        
    def editTask(self, p_TaskId, p_TaskText):
        session = self.session()
        
        query = session.query(Task).filter(Task.id==p_TaskId)
        
        task = query.first()
        task.tasktext = p_TaskText
        
        session.update(task)
        session.commit()
        
    def getAllCategories(self):
        session = self.session()
        
        categories = []
        
        for cat in session.query(Category):
            categories.append(cat)
            
        return categories
        
    def getTasksByCategory(self, p_Category):
        session = self.session()
        
        tasks = []
        
        for task in session.query(Task).filter_by(category_id=p_Category.id):
            tasks.append(task)
            
        return tasks
        
        
    def deleteAllCategories(self):
        session = self.session()
        #FIXME this is better implemented as a cascade operation
        for cat in session.query(Category):
            session.delete(cat)
            for task in cat.tasks:
                session.delete(task)
            
        session.commit()
            
