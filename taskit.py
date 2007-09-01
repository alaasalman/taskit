#! /usr/bin/python

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from GTDWindow import GTDWindow

    
def main(args):
  app = QtGui.QApplication(sys.argv)
  
  window = GTDWindow()
  
  window.show()
  app.exec_()


if(__name__ == "__main__"):
  main(sys.argv)
