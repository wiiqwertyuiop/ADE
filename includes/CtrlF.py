# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out/CtrlF.ui'
#
# Created: Sat Aug 24 17:15:24 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!
#

from PyQt4.QtGui import *  
from PyQt4.QtCore import *
import ClickQLabel

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form, main):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(370, 128)
        Form.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        
        #Form.setFocusPolicy(Qt.StrongFocus)
        
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(10, 10, 46, 13))
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QRect(10, 30, 241, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setText(main.word)
        self.lineEdit.textChanged.connect(self.LineEdit)
        
        self.checkBox = QCheckBox(Form)
        self.checkBox.setGeometry(QRect(10, 60, 81, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.setChecked(main.case)
        
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setGeometry(QRect(10, 80, 131, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_2.setChecked(main.whole)
        
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setGeometry(QRect(10, 100, 91, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_3.setChecked(main.regex)
        
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(280, 10, 81, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))        
        self.pushButton.clicked.connect(lambda: self.FindNext(Form, main))
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setGeometry(QRect(280, 40, 81, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: self.FindPrev(Form, main))
        
        if self.lineEdit.text().isEmpty():
          self.pushButton.setDisabled(1)
          self.pushButton_2.setDisabled(1)
        else:
          self.pushButton.setDisabled(0)
          self.pushButton_2.setDisabled(0)
        
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setGeometry(QRect(280, 70, 81, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(Form.close)
        
        self.label_2 = ClickQLabel.Label(Form)
        self.label_2.setGeometry(QRect(160, 100, 111, 16))
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);\n"
"text-decoration: underline;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Form.connect(self.label_2, SIGNAL('clicked()'), lambda: self.Click(main))  

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Find Text", None))
        self.label.setText(_translate("Form", "Find:", None))
        self.pushButton.setText(_translate("Form", "Find Next", None))
        self.pushButton_3.setText(_translate("Form", "Close", None))
        self.pushButton_2.setText(_translate("Form", "Find Previous", None))
        self.checkBox.setText(_translate("Form", "Match case", None))
        self.checkBox_2.setText(_translate("Form", "Match whole word only", None))
        self.checkBox_3.setText(_translate("Form", "Regex search", None))
        self.label_2.setText(_translate("Form", "Goto Replace (Ctrl+H)", None))
    
    def Click(self, main):
      main.ReplaceDialog()
      
    def LineEdit(self):
    
      if self.lineEdit.text().isEmpty():
        self.pushButton.setDisabled(1)
        self.pushButton_2.setDisabled(1)
      else:
        self.pushButton.setDisabled(0)
        self.pushButton_2.setDisabled(0)
      
    def FindNext(self, Form, main):
      
      main.word = self.lineEdit.text()
      main.case = self.checkBox.isChecked()
      main.whole = self.checkBox_2.isChecked()
      main.regex = self.checkBox_3.isChecked()
        
      if not main.FindText(0, 0):
        if QMessageBox.warning(Form, 'Warning', "The text could not be found!\n\nSearch from begining?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
          if not main.FindText(0, 1):
            QMessageBox.warning(Form, 'Warning', "The text could not be found!")

    def FindPrev(self, Form, main):      
      
      main.word = self.lineEdit.text()
      main.case = self.checkBox.isChecked()
      main.whole = self.checkBox_2.isChecked()
      main.regex = self.checkBox_3.isChecked()
        
      if not main.FindText(1, 0):
        if QMessageBox.warning(Form, 'Warning', "The text could not be found!\n\nSearch from end?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
          if not main.FindText(1, 2):
            QMessageBox.warning(Form, 'Warning', "The text could not be found!")
            
class MainWindow(QWidget):
  def __init__(self, main):
    QWidget.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self, main)