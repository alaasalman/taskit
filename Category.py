class Category(object):
    
    def __init__(self, p_CategoryTitle):
        self.categorytitle = p_CategoryTitle

    def __repr__(self):
        #return "Category(%d, %r)" % (self.id, self.categorytitle)
        return "Category(%r)" % (self.categorytitle)
