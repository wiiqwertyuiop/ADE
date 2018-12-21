####################
## Syntax edit window
##
## Makes it easier to edit syntax related things in the cfg file
####################

import cfg
import SyntaxHighlighting
#from ADE import Config
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

######################################
##
## Create window

    def setupUi(self, Form, text, Config):
        Form.setObjectName(_fromUtf8("Syntax Highlighting Editor"))
        Form.resize(301, 338)
        Form.setWindowIcon(QIcon('includes/imgs/icon.png'))
        Form.setAttribute( Qt.WA_QuitOnClose, False );    # close this window when the mainwindow gets closed
        
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        #self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 271, 51))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setPlainText(cfg.get("SyntaxHighlighting", "Opcodes"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 6)
        
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(Form)
        #self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 130, 271, 51))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_2.setPlainText(cfg.get("SyntaxHighlighting", "Keywords"))
        self.gridLayout_2.addWidget(self.plainTextEdit_2, 3, 0, 1, 6)
        
        self.checkBox = QtGui.QCheckBox(Form)
        #self.checkBox.setGeometry(QtCore.QRect(100, 20, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))        
        self.checkBox.setChecked(cfg.getBool("SyntaxHighlighting", "opBold"))
        self.gridLayout_2.addWidget(self.checkBox, 0, 2, 1, 1)
        
        self.checkBox_2 = QtGui.QCheckBox(Form)
        #self.checkBox_2.setGeometry(QtCore.QRect(150, 20, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_2.setChecked(cfg.getBool("SyntaxHighlighting", "opUnderline"))
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 3, 1, 2)
        
        self.checkBox_3 = QtGui.QCheckBox(Form)
        #self.checkBox_3.setGeometry(QtCore.QRect(230, 20, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_3.setChecked(cfg.getBool("SyntaxHighlighting", "opItalic"))
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 5, 1, 1)
        
        self.checkBox_4 = QtGui.QCheckBox(Form)
        #self.checkBox_4.setGeometry(QtCore.QRect(100, 110, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_4.setChecked(cfg.getBool("SyntaxHighlighting", "keyBold"))
        self.gridLayout_2.addWidget(self.checkBox_4, 2, 3, 1, 2)
        
        self.checkBox_5 = QtGui.QCheckBox(Form)
        #self.checkBox_5.setGeometry(QtCore.QRect(150, 110, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_5.setChecked(cfg.getBool("SyntaxHighlighting", "keyUnderline"))
        self.gridLayout_2.addWidget(self.checkBox_5, 2, 2, 1, 1)
        
        self.checkBox_6 = QtGui.QCheckBox(Form)
        #self.checkBox_6.setGeometry(QtCore.QRect(230, 110, 70, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_6.setChecked(cfg.getBool("SyntaxHighlighting", "keyItalic"))
        self.gridLayout_2.addWidget(self.checkBox_6, 2, 5, 1, 1)
        
        self.label = QtGui.QLabel(Form)
        #self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        
        self.label_2 = QtGui.QLabel(Form)
        #self.label_2.setGeometry(QtCore.QRect(10, 110, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QtGui.QLabel(Form)
        #self.label_3.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        
        self.label_4 = QtGui.QLabel(Form)
        #self.label_4.setGeometry(QtCore.QRect(10, 230, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        
        self.label_5 = QtGui.QLabel(Form)
        #self.label_5.setGeometry(QtCore.QRect(10, 260, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        
        self.checkBox_7 = QtGui.QCheckBox(Form)
        #self.checkBox_7.setGeometry(QtCore.QRect(100, 200, 70, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_7.setChecked(cfg.getBool("SyntaxHighlighting", "cmntBold"))
        self.gridLayout_2.addWidget(self.checkBox_7, 4, 2, 1, 1)
        
        self.checkBox_8 = QtGui.QCheckBox(Form)
        #self.checkBox_8.setGeometry(QtCore.QRect(150, 200, 70, 17))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_8.setChecked(cfg.getBool("SyntaxHighlighting", "cmntUnderline"))
        self.gridLayout_2.addWidget(self.checkBox_8, 4, 3, 1, 2)
        
        self.checkBox_9 = QtGui.QCheckBox(Form)
        #self.checkBox_9.setGeometry(QtCore.QRect(230, 200, 70, 17))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_9.setChecked(cfg.getBool("SyntaxHighlighting", "cmntItalic"))
        self.gridLayout_2.addWidget(self.checkBox_9, 4, 5, 1, 1)
        
        self.checkBox_10 = QtGui.QCheckBox(Form)
        #self.checkBox_10.setGeometry(QtCore.QRect(100, 230, 70, 17))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox_10.setChecked(cfg.getBool("SyntaxHighlighting", "addrBold"))
        self.gridLayout_2.addWidget(self.checkBox_10, 5, 5, 1, 1)
        
        self.checkBox_11 = QtGui.QCheckBox(Form)
        #self.checkBox_11.setGeometry(QtCore.QRect(150, 230, 70, 17))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox_11.setChecked(cfg.getBool("SyntaxHighlighting", "addrUnderline"))
        self.gridLayout_2.addWidget(self.checkBox_11, 5, 2, 1, 1)
        
        self.checkBox_12 = QtGui.QCheckBox(Form)
        #self.checkBox_12.setGeometry(QtCore.QRect(230, 230, 70, 17))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_12.setChecked(cfg.getBool("SyntaxHighlighting", "addrItalic"))
        self.gridLayout_2.addWidget(self.checkBox_12, 5, 3, 1, 2)
        
        self.checkBox_13 = QtGui.QCheckBox(Form)
        #self.checkBox_13.setGeometry(QtCore.QRect(100, 260, 70, 17))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.checkBox_13.setChecked(cfg.getBool("SyntaxHighlighting", "lblBold"))
        self.gridLayout_2.addWidget(self.checkBox_13, 6, 3, 1, 2)
        
        self.checkBox_14 = QtGui.QCheckBox(Form)
        #self.checkBox_14.setGeometry(QtCore.QRect(150, 260, 70, 17))
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.checkBox_14.setChecked(cfg.getBool("SyntaxHighlighting", "lblUnderline"))
        self.gridLayout_2.addWidget(self.checkBox_14, 6, 5, 1, 1)
        
        self.checkBox_15 = QtGui.QCheckBox(Form)
        #self.checkBox_15.setGeometry(QtCore.QRect(230, 260, 70, 17))
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.checkBox_15.setChecked(cfg.getBool("SyntaxHighlighting", "lblItalic"))
        self.gridLayout_2.addWidget(self.checkBox_15, 6, 2, 1, 1)
        
        self.pushButton = QtGui.QPushButton(Form)
        #self.pushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton.setMaximumSize(QtCore.QSize(16, 16))
        #self.pushButton.setGeometry(QtCore.QRect(70, 20, 16, 16))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb( " + 
        str(cfg.getInt("SyntaxHighlighting", "opR")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "opG")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "opB")) + " );"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: self.changeColor(self.pushButton))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
                
        self.pushButton_2 = QtGui.QPushButton(Form)
        #self.pushButton_2.setGeometry(QtCore.QRect(70, 110, 16, 16))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb( " + 
        str(cfg.getInt("SyntaxHighlighting", "keyR")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "keyG")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "keyB")) + " );"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: self.changeColor(self.pushButton_2))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        #self.pushButton_3.setGeometry(QtCore.QRect(70, 200, 16, 16))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb( " + 
        str(cfg.getInt("SyntaxHighlighting", "cmntR")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "cmntG")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "cmntB")) + " );"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(lambda: self.changeColor(self.pushButton_3))
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 1, 1, 1)
        
        self.pushButton_4 = QtGui.QPushButton(Form)
        #self.pushButton_4.setGeometry(QtCore.QRect(70, 230, 16, 16))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb( " + 
        str(cfg.getInt("SyntaxHighlighting", "addrR")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "addrG")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "addrB")) + " );"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda: self.changeColor(self.pushButton_4))
        self.gridLayout_2.addWidget(self.pushButton_4, 5, 1, 1, 1)
        
        self.pushButton_5 = QtGui.QPushButton(Form)
        #self.pushButton_5.setGeometry(QtCore.QRect(70, 260, 16, 16))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb( " + 
        str(cfg.getInt("SyntaxHighlighting", "lblR")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "lblG")) + " , " + 
        str(cfg.getInt("SyntaxHighlighting", "lblB")) + " );"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(lambda: self.changeColor(self.pushButton_5))
        self.gridLayout_2.addWidget(self.pushButton_5, 6, 1, 1, 1)
        
        self.pushButton_6 = QtGui.QPushButton(Form)
        #self.pushButton_6.setGeometry(QtCore.QRect(130, 300, 71, 23))
        self.pushButton_6.setStyleSheet(_fromUtf8(""))
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(lambda: self.saveChanges(Form, text, Config))
        self.gridLayout_2.addWidget(self.pushButton_6, 7, 2, 1, 2)

        self.pushButton_7 = QtGui.QPushButton(Form)
        #self.pushButton_7.setGeometry(QtCore.QRect(210, 300, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.clicked.connect(Form.close)
        self.gridLayout_2.addWidget(self.pushButton_7, 7, 4, 1, 2)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Syntax Highlighting Editor", None))
        self.checkBox.setText(_translate("Form", "Bold", None))
        self.checkBox_2.setText(_translate("Form", "Underline", None))
        self.checkBox_3.setText(_translate("Form", "Italic", None))
        self.checkBox_4.setText(_translate("Form", "Bold", None))        
        self.checkBox_5.setText(_translate("Form", "Underline", None))
        self.checkBox_6.setText(_translate("Form", "Italic", None))
        self.label.setText(_translate("Form", "Opcodes", None))
        self.label_2.setText(_translate("Form", "Keywords", None))
        self.label_3.setText(_translate("Form", "Comments", None))
        self.label_4.setText(_translate("Form", "Address", None))
        self.label_5.setText(_translate("Form", "Labels", None))
        self.checkBox_7.setText(_translate("Form", "Bold", None))
        self.checkBox_8.setText(_translate("Form", "Underline", None))
        self.checkBox_9.setText(_translate("Form", "Italic", None))
        self.checkBox_10.setText(_translate("Form", "Bold", None))
        self.checkBox_11.setText(_translate("Form", "Underline", None))
        self.checkBox_12.setText(_translate("Form", "Italic", None))
        self.checkBox_13.setText(_translate("Form", "Bold", None))
        self.checkBox_14.setText(_translate("Form", "Underline", None))
        self.checkBox_15.setText(_translate("Form", "Italic", None))
        self.pushButton_6.setText(_translate("Form", "Save", None))
        self.pushButton_7.setText(_translate("Form", "Cancel", None))
        
######################################
##
## Functions

    def saveChanges(self, Form, text, Config):
      cfgfile = open("config.ini",'w')
      
      try:
        Config.add_section('SyntaxHighlighting')
      except:
        pass
      
      color = str(self.pushButton.styleSheet())
      color = color.split( );
      
      Config.set('SyntaxHighlighting','opR', color[2])
      Config.set('SyntaxHighlighting','opG', color[4])
      Config.set('SyntaxHighlighting','opB', color[6])
      
      if self.checkBox.isChecked():
        Config.set('SyntaxHighlighting','opBold', "1")
      else:
        Config.set('SyntaxHighlighting','opBold', "0")
        
      if self.checkBox_2.isChecked():
        Config.set('SyntaxHighlighting','opUnderline', "1")
      else:
        Config.set('SyntaxHighlighting','opUnderline', "0")

      if self.checkBox_3.isChecked():
        Config.set('SyntaxHighlighting','opItalic', "1")
      else:
        Config.set('SyntaxHighlighting','opItalic', "0")
      
      Config.set('SyntaxHighlighting','opcodes', self.plainTextEdit.toPlainText())

      color = str(self.pushButton_2.styleSheet())
      color = color.split( );
      
      Config.set('SyntaxHighlighting','keyR', color[2])
      Config.set('SyntaxHighlighting','keyG', color[4])
      Config.set('SyntaxHighlighting','keyB', color[6])
      
      if self.checkBox_4.isChecked():
        Config.set('SyntaxHighlighting','keyBold', "1")
      else:
        Config.set('SyntaxHighlighting','keyBold', "0")
        
      if self.checkBox_5.isChecked():
        Config.set('SyntaxHighlighting','keyUnderline', "1")
      else:
        Config.set('SyntaxHighlighting','keyUnderline', "0")

      if self.checkBox_6.isChecked():
        Config.set('SyntaxHighlighting','keyItalic', "1")
      else:
        Config.set('SyntaxHighlighting','keyItalic', "0")
      
      Config.set('SyntaxHighlighting','keywords', self.plainTextEdit_2.toPlainText())
      
      color = str(self.pushButton_3.styleSheet())
      color = color.split( );
      
      Config.set('SyntaxHighlighting','cmntR', color[2])
      Config.set('SyntaxHighlighting','cmntG', color[4])
      Config.set('SyntaxHighlighting','cmntB', color[6])
      
      if self.checkBox_7.isChecked():
        Config.set('SyntaxHighlighting','cmntBold', "1")
      else:
        Config.set('SyntaxHighlighting','cmntBold', "0")
        
      if self.checkBox_8.isChecked():
        Config.set('SyntaxHighlighting','cmntUnderline', "1")
      else:
        Config.set('SyntaxHighlighting','cmntUnderline', "0")

      if self.checkBox_9.isChecked():
        Config.set('SyntaxHighlighting','cmntItalic', "1")
      else:
        Config.set('SyntaxHighlighting','cmntItalic', "0")

      color = str(self.pushButton_4.styleSheet())
      color = color.split( );
      
      Config.set('SyntaxHighlighting','addrR', color[2])
      Config.set('SyntaxHighlighting','addrG', color[4])
      Config.set('SyntaxHighlighting','addrB', color[6])
      
      if self.checkBox_10.isChecked():
        Config.set('SyntaxHighlighting','addrBold', "1")
      else:
        Config.set('SyntaxHighlighting','addrBold', "0")
        
      if self.checkBox_11.isChecked():
        Config.set('SyntaxHighlighting','addrUnderline', "1")
      else:
        Config.set('SyntaxHighlighting','addrUnderline', "0")

      if self.checkBox_12.isChecked():
        Config.set('SyntaxHighlighting','addrItalic', "1")
      else:
        Config.set('SyntaxHighlighting','addrItalic', "0")
        
      color = str(self.pushButton_5.styleSheet())
      color = color.split( );
      
      Config.set('SyntaxHighlighting','lblR', color[2])
      Config.set('SyntaxHighlighting','lblG', color[4])
      Config.set('SyntaxHighlighting','lblB', color[6])
      
      if self.checkBox_7.isChecked():
        Config.set('SyntaxHighlighting','lblBold', "1")
      else:
        Config.set('SyntaxHighlighting','lblBold', "0")
        
      if self.checkBox_8.isChecked():
        Config.set('SyntaxHighlighting','lblUnderline', "1")
      else:
        Config.set('SyntaxHighlighting','lblUnderline', "0")

      if self.checkBox_9.isChecked():
        Config.set('SyntaxHighlighting','lblItalic', "1")
      else:
        Config.set('SyntaxHighlighting','lblItalic', "0")
                              
      Config.write(cfgfile)
      cfgfile.close()
      
      if cfg.getBool('SyntaxHighlighting', 'On'):
        numb = len(text)
        i = 0
        while i != numb:
          SyntaxHighlighting.Highlighter(text[i], "Classic" ) # add syntax highliting to text area
          i += 1
      
      Form.close()
      
    def changeColor(self, button):
      col = QtGui.QColorDialog.getColor()      
      if col.isValid():            
            button.setStyleSheet("background-color: rgb( %s , %s , %s )"
                % (col.red(), col.green(), col.blue()))
##
##
######################################

class MainWindow(QWidget):
  def __init__(self, text, Config):
    QWidget.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self, text, Config)
        