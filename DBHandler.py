from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm import relation

from Task import Task
from Category import Category

class DBHandler():
    def __init__(self):
        engine = create_engine("sqlite:///tasklist.db", echo=True)
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
            
