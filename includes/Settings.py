# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out/Settings.ui'
#
# Created: Thu Oct 03 15:25:40 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

import cfg
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
    def setupUi(self, Form, main, Config):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(410, 383)
        Form.setWindowIcon(QIcon('includes/imgs/icon.png'))
        Form.setWindowFlags(Qt.Window)
        Form.setAttribute( Qt.WA_QuitOnClose, False );    # close this window when the mainwindow gets closed
        
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.lineEdit_3 = QLineEdit(Form)
        #self.lineEdit_3.setGeometry(QRect(20, 140, 181, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 4, 0, 1, 2)
        
        text = main.Emulator
        if text == "":
          text = cfg.get("CMD", "Emulator")
        self.lineEdit_3.setText(text)
        
        self.lineEdit_4 = QLineEdit(Form)
        #self.lineEdit_4.setGeometry(QRect(20, 190, 181, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 6, 0, 1, 2)
        
        text = main.Debugger
        if text == "":
          text = cfg.get("CMD", "Debugger")
        self.lineEdit_4.setText(text)
        
        self.lineEdit_5 = QLineEdit(Form)
        #self.lineEdit_5.setGeometry(QRect(20, 290, 181, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 10, 0, 1, 2)
        
        text = main.Maps
        if text == "":
          text = cfg.get("CMD", "Maps")
        self.lineEdit_5.setText(text)
        
        self.lineEdit_6 = QLineEdit(Form)
        #self.lineEdit_6.setGeometry(QRect(20, 240, 181, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 8, 0, 1, 2)
        
        text = main.ROM
        if text == "":
          text = cfg.get("CMD", "ROM")
        self.lineEdit_6.setText(text)
        
        self.textEdit = QTextEdit(Form)
        #self.textEdit.setGeometry(QRect(20, 40, 261, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 2, 3)
        
        text = main.CMDS
        if text == "":
          text = cfg.get("CMD", "CMDS")
        self.textEdit.setText(text)
        
        self.pushButton = QPushButton(Form)
        #self.pushButton.setGeometry(QRect(300, 50, 75, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: self.Append(Form))
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        
        self.pushButton_3 = QPushButton(Form)
        #self.pushButton_3.setGeometry(QRect(210, 140, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(lambda: self.Browse(Form, self.lineEdit_3))
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        
        self.pushButton_4 = QPushButton(Form)
        #self.pushButton_4.setGeometry(QRect(210, 190, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda: self.Browse(Form, self.lineEdit_4))
        self.gridLayout.addWidget(self.pushButton_4, 6, 2, 1, 1)
        
        self.pushButton_9 = QPushButton(Form)
        #self.pushButton_9.setGeometry(QRect(210, 290, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.clicked.connect(lambda: self.Browse(Form, self.lineEdit_5))
        self.gridLayout.addWidget(self.pushButton_9, 10, 2, 1, 1)
        
        self.pushButton_12 = QPushButton(Form)
        #self.pushButton_12.setGeometry(QRect(210, 240, 75, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_12.clicked.connect(lambda: self.Browse(Form, self.lineEdit_6))
        self.gridLayout.addWidget(self.pushButton_12, 8, 2, 1, 1)
        
        # set as defualt
        self.pushButton_5 = QPushButton(Form)
        #self.pushButton_5.setGeometry(QRect(300, 90, 91, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(lambda: self.Default(Form, self.textEdit.toPlainText(), "CMDS", Config, main))
        self.gridLayout.addWidget(self.pushButton_5, 2, 3, 1, 1)
        
        self.pushButton_6 = QPushButton(Form)
        #self.pushButton_6.setGeometry(QRect(300, 140, 91, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(lambda: self.Default(Form, self.lineEdit_3.text(), "Emulator", Config, main))
        self.gridLayout.addWidget(self.pushButton_6, 4, 3, 1, 1)
        
        self.pushButton_7 = QPushButton(Form)
        #self.pushButton_7.setGeometry(QRect(300, 190, 91, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.clicked.connect(lambda: self.Default(Form, self.lineEdit_4.text(), "Debugger", Config, main))
        self.gridLayout.addWidget(self.pushButton_7, 6, 3, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        #self.pushButton_11.setGeometry(QRect(300, 240, 91, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_11.clicked.connect(lambda: self.Default(Form, self.lineEdit_6.text(), "ROM", Config, main))
        self.gridLayout.addWidget(self.pushButton_11, 8, 3, 1, 1)
        
        self.pushButton_8 = QPushButton(Form)
        #self.pushButton_8.setGeometry(QRect(300, 290, 91, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))        
        self.pushButton_8.clicked.connect(lambda: self.Default(Form, self.lineEdit_5.text(), "Maps", Config, main))
        self.gridLayout.addWidget(self.pushButton_8, 10, 3, 1, 1)
        
        self.label = QLabel(Form)
        #self.label.setGeometry(QRect(20, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.label_3 = QLabel(Form)
        #self.label_3.setGeometry(QRect(20, 120, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.label_4 = QLabel(Form)
        #self.label_4.setGeometry(QRect(20, 170, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        
        self.label_5 = QLabel(Form)
        #self.label_5.setGeometry(QRect(20, 270, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        
        self.label_6 = QLabel(Form)
        #self.label_6.setGeometry(QRect(20, 220, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.pushButton_2 = QPushButton(Form)
        #self.pushButton_2.setGeometry(QRect(210, 340, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: self.Ok(Form, main))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        
        self.pushButton_10 = QPushButton(Form)
        #self.pushButton_10.setGeometry(QRect(310, 340, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_10.clicked.connect(Form.close)
        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 11, 3, 2, 1)
        
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        
        
      
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Build Settings", None))
        self.pushButton.setText(_translate("Form", "Append...", None))
        self.label.setText(_translate("Form", "Command Line:", None))
        self.label_3.setText(_translate("Form", "Emulator:", None))
        self.pushButton_3.setText(_translate("Form", "Browse...", None))
        self.label_4.setText(_translate("Form", "Debugger:", None))
        self.pushButton_4.setText(_translate("Form", "Browse...", None))
        self.pushButton_5.setText(_translate("Form", "Set as default...", None))
        self.pushButton_6.setText(_translate("Form", "Set as default...", None))
        self.pushButton_7.setText(_translate("Form", "Set as default...", None))
        self.pushButton_8.setText(_translate("Form", "Set as default...", None))
        self.label_5.setText(_translate("Form", "RAM/ROM Map:", None))
        self.pushButton_9.setText(_translate("Form", "Browse...", None))
        self.pushButton_2.setText(_translate("Form", "Ok", None))
        self.pushButton_10.setText(_translate("Form", "Cancel", None))
        self.pushButton_11.setText(_translate("Form", "Set as default...", None))
        self.label_6.setText(_translate("Form", "ROM (for emulators):", None))
        self.pushButton_12.setText(_translate("Form", "Browse...", None))
        
        
##############################
##
##

    def Append(self, Form):
      path = QFileDialog.getOpenFileName(Form, 'Select a file')
      if path != "": self.textEdit.append(path)
    
    def Browse(self, Form, Line):
      path = QFileDialog.getOpenFileName(Form, 'Select a file')
      if path != "": Line.setText(path)

    def Default(self, Form, Line, Save, Config, main):
      
      cfgfile = open("config.ini",'w')  # open config file for writing
      
      try:
        Config.add_section('CMD')
      except:
        pass
      
      if Save == "CMDS":
        main.CMDS = self.textEdit.toPlainText()
      elif Save == "Emulator":
        main.Emulator = self.lineEdit_3.text()
      elif Save == "Debugger":
        main.Debugger = self.lineEdit_4.text()
      else:
        main.Maps = self.lineEdit_5.text()

      Config.set('CMD', Save, Line)
       
      Config.write(cfgfile)
      cfgfile.close()
    
    def Ok(self, Form, main):
      main.CMDS = self.textEdit.toPlainText()
      main.Emulator = self.lineEdit_3.text()
      main.Debugger = self.lineEdit_4.text()
      main.Maps = self.lineEdit_5.text()
      main.ROM = self.lineEdit_6.text()
      Form.close()
##
##############################

class MainWindow(QDialog):
  def __init__(self, main, Config):
    QWidget.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self, main, Config)
