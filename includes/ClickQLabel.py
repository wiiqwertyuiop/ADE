from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
  
class Label(QLabel):  
      
    def __init(self, parent):  
        QLabel.__init__(self, parent)  
       
    def mouseReleaseEvent(self, ev):  
        self.emit(SIGNAL('clicked()')) 