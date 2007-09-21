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

class Task(object):
    
    def __init__(self, p_TaskText, p_CategoryId=0):
        self.tasktext = p_TaskText
        self.category_id = p_CategoryId
      
    def __repr__(self):
        #return "Task(%d, %d, %r)" % (self.id, self.category_id, self.tasktext)
        return "Task(%r)" % (self.tasktext)
