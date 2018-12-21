# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out/untitled.ui'
#
# Created: Sun Sep 08 16:41:55 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4.Qt import *
from PyQt4.QtCore import *

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
        Form.setFixedSize(235, 93)
        Form.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QRect(10, 30, 211, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(10, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(50, 60, 75, 23))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: main.Goto(self.lineEdit))
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setGeometry(QRect(140, 60, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Go to line", None))
        self.pushButton.setText(_translate("Form", "Goto", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.label.setText(_translate("Form", "Line number:", None))

class MainWindow(QWidget):
  def __init__(self, main):
    QWidget.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self, main)