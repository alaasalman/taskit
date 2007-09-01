class Task(object):
    
    def __init__(self, p_TaskText, p_CategoryId=0):
        self.tasktext = p_TaskText
        self.category_id = p_CategoryId
      
    def __repr__(self):
        #return "Task(%d, %d, %r)" % (self.id, self.category_id, self.tasktext)
        return "Task(%r)" % (self.tasktext)
