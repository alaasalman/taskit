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

from ui import AboutDialog

class TIAboutDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        self.ui = AboutDialog.Ui_Dialog()
        self.ui.setupUi(self)
        
        htmlAboutAuthor = """<html>
            <body>
                TaskIt GTD Application.
                <p>Author: Alaa Salman</p>
                <p>Uses the awesome famfamfam icons.</p>
            </body>
        </html>
        """
        
        htmlAboutLicense = """<html><body>TaskIt is free software; you can redistribute it and/or modify
                                it under the terms of the GNU General Public License as published by
                                the Free Software Foundation; either version 3 of the License, or
                                (at your option) any later version.

                                <p>TaskIt is distributed in the hope that it will be useful,
                                but WITHOUT ANY WARRANTY; without even the implied warranty of
                                MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
                                GNU General Public License for more details.</p>

                                <p>You should have received a copy of the GNU General Public License
                                along with this program.  If not, see http://www.gnu.org/licenses</p>
                                <p></p></body></html>"""
        
        self.ui.tabWidget.widget(0).findChild(QtGui.QTextBrowser, "authorTextBrowser").setHtml(htmlAboutAuthor)
        self.ui.tabWidget.widget(1).findChild(QtGui.QTextBrowser, "licenseTextBrowser").setHtml(htmlAboutLicense)
        
        
