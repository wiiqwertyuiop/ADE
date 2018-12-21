#!/usr/bin/env
####################
## ASM Development Environment
##           by
##      wiiqwertyuiop
##
## A open source assembly editor made specifically for SNES ASM.
##
## TODO:
##
## Version info:
##
## V1.0:
##  - Customizable syntax highlighting (with a option to turn it off)
##  - Line numbers
##  - Completely customizable insertable templates
##  - Can open files by default
##  - Tabs
####################

import sys

if sys.version_info[:3] != (2,7,5):
    print 'Python 2.7.5 is not being used; it has only been tested that version.'

import os
import re
import subprocess

import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read(os.path.join(os.path.abspath(os.path.dirname(__file__))) + "/config.ini")

text = {} # dict of text boxes
savepaths = {} # paths where each file is saved

import includes.cfg
import includes.TextEdit
import includes.SyntaxHighlighting
import includes.SyntaxEditWindow
import includes.CtrlF
import includes.CtrlH
import includes.CtrlG
import includes.Settings


from PyQt4.Qt import *
from PyQt4.QtGui import *

class Notepad(QMainWindow):
  
  def __init__(self):
      super(Notepad, self).__init__()
      
      self.word = ""  # last word searched for
      self.case = 0   # match case
      self.whole = 0  # match whole word
      self.regex = 0  # regex search
      self.replace = "" # last replaced
      
      self.CMDS = ""
      self.Emulator = ""
      self.Debugger = ""
      self.ROM = ""
      self.Maps = ""
      
      #self.CanSet = 0 # tells if we cancled editing the settings or not
      
      self.PROJ = ""
      
      self.busy = 0
      self.ASDone = 0
      self.initUI()
      
      
  def initUI(self):
      
    # Create tab widget
    self.tab_widget = QTabWidget(self)
    self.setCentralWidget(self.tab_widget)
    self.tab_widget.currentChanged.connect(self.cursorPositionChanged)
    
    # make the tabs closeable
    self.tab_widget.setTabsClosable(1)
    self.tab_widget.tabCloseRequested.connect(self.removeTab)
    
    # create menubar
    self.menubar = self.menuBar()
    fileMenu = self.menubar.addMenu('&File')
    fileMenu.aboutToShow.connect(self.FileInit)
    
    # Create options in file menu
    newAction = QAction('New', self)
    newAction.setShortcut('Ctrl+N')
    newAction.setStatusTip('Create new file')
    newAction.triggered.connect(lambda: self.newTab())
    
    saveAction = QAction('Save', self)
    saveAction.setShortcut('Ctrl+S')
    saveAction.setStatusTip('Save current file')
    saveAction.triggered.connect(lambda: self.saveFile(0))
    
    saveAction2 = QAction('Save As', self)
    #saveAction2.setShortcut('Ctrl+Shift+S')
    saveAction2.setStatusTip('Save current file as')
    saveAction2.triggered.connect(lambda: self.saveFile())
    
    
    NewProj = QAction('New Project', self)
    NewProj.setStatusTip('Create Prjoect')
    NewProj.triggered.connect(self.newProject)
    
    OpenProj = QAction('Open Project', self)
    OpenProj.setStatusTip('Open Project')
    OpenProj.triggered.connect(lambda: self.openProject())
    
    self.CloseProj = QAction('Close Project', self)
    self.CloseProj.setStatusTip('Close Project')
    self.CloseProj.triggered.connect(self.closeProject)
    
    
    saveAction3 = QAction('Save All', self)
    saveAction3.setShortcut('Ctrl+Shift+S')
    saveAction3.setStatusTip('Saves all files')
    saveAction3.triggered.connect(self.saveAll)
    
    closeAll = QAction('Close All', self)
    closeAll.setShortcut('Ctrl+Shift+C')
    closeAll.setStatusTip('Closes all files')
    closeAll.triggered.connect(self.closeAll)
    
    openAction = QAction('Open', self)
    openAction.setShortcut('Ctrl+O')
    openAction.setStatusTip('Open a file')
    openAction.triggered.connect(lambda: self.openFile())
    
    closeAction = QAction('Quit', self)
    closeAction.setShortcut('Ctrl+Q')
    closeAction.setStatusTip('Close ADE')
    closeAction.triggered.connect(self.close)
    
    fileMenu.addAction(newAction)
    fileMenu.addAction(openAction)
    fileMenu.addAction(saveAction)
    fileMenu.addAction(saveAction2)
    fileMenu.addSeparator()
    fileMenu.addAction(NewProj)
    fileMenu.addAction(OpenProj)
    fileMenu.addAction(self.CloseProj)
    fileMenu.addSeparator()
    fileMenu.addAction(saveAction3)
    fileMenu.addAction(closeAll)
    fileMenu.addSeparator()
    fileMenu.addAction(closeAction)
    
    # create edit menu
    edit_menu = self.menubar.addMenu('&Edit')
    edit_menu.aboutToShow.connect(self.EditInit)
    
    self.UndoAction = QAction('Undo', self)
    self.UndoAction.setShortcut('Ctrl+Z')
    self.UndoAction.setStatusTip('Undo action')
    self.UndoAction.setDisabled(1)
    self.UndoAction.triggered.connect(self.Undo)
    
    self.RedoAction = QAction('Redo', self)
    self.RedoAction.setShortcut('Ctrl+Y')
    self.RedoAction.setStatusTip('Redo action')
    self.RedoAction.triggered.connect(self.Redo)

    self.CutAction = QAction('Cut', self)
    self.CutAction.setShortcut('Ctrl+X')
    self.CutAction.setStatusTip('Cut text')
    self.CutAction.triggered.connect(self.Cut)
    
    self.CopyAction = QAction('Copy', self)
    self.CopyAction.setShortcut('Ctrl+C')
    self.CopyAction.setStatusTip('Copy text')
    self.CopyAction.triggered.connect(self.Copy)
    
    self.PasteAction = QAction('Paste', self)
    self.PasteAction.setShortcut('Ctrl+V')
    self.PasteAction.setStatusTip('Paste text')
    self.PasteAction.triggered.connect(self.Paste)
    
    self.SelectAllAction = QAction('Select All', self)
    self.SelectAllAction.setShortcut('Ctrl+A')
    self.SelectAllAction.setStatusTip('Select All text')
    self.SelectAllAction.triggered.connect(self.SelectAll)
    
    self.FindAction = QAction('Find', self)
    self.FindAction.setShortcut('Ctrl+F')
    self.FindAction.setStatusTip('Find text')
    self.FindAction.triggered.connect(self.FindDialog)
    
    self.ReplaceAction = QAction('Replace', self)
    self.ReplaceAction.setShortcut('Ctrl+H')
    self.ReplaceAction.setStatusTip('Find/replace text')
    self.ReplaceAction.triggered.connect(self.ReplaceDialog)

    self.ReplaceNAction = QAction('Replace Next', self)
    self.ReplaceNAction.setShortcut('F4')
    self.ReplaceNAction.setStatusTip('Replace text')
    self.ReplaceNAction.triggered.connect(self.Replace)
    
    self.FindNAction = QAction('Find Next', self)
    self.FindNAction.setShortcut('F3')
    self.FindNAction.setStatusTip('Find next word')
    self.FindNAction.triggered.connect(self.FindNext)
    
    self.FindPAction = QAction('Find Previous', self)
    self.FindPAction.setShortcut('Shift+F3')
    self.FindPAction.setStatusTip('Find previous word')
    self.FindPAction.triggered.connect(self.FindPrev)

    self.GotoAction = QAction('Goto...', self)
    self.GotoAction.setShortcut('Ctrl+G')
    self.GotoAction.setStatusTip('Go to a specific line')
    self.GotoAction.triggered.connect(self.GotoDialog)
    
    edit_menu.addAction(self.UndoAction)
    edit_menu.addAction(self.RedoAction)
    edit_menu.addSeparator()
    edit_menu.addAction(self.CutAction)
    edit_menu.addAction(self.CopyAction)
    edit_menu.addAction(self.PasteAction)
    edit_menu.addAction(self.SelectAllAction)
    edit_menu.addSeparator()
    edit_menu.addAction(self.FindAction)
    edit_menu.addAction(self.FindNAction)
    edit_menu.addAction(self.FindPAction)
    edit_menu.addAction(self.ReplaceAction)
    edit_menu.addAction(self.ReplaceNAction)
    edit_menu.addAction(self.GotoAction)

    # create build menu
    build_menu = self.menubar.addMenu('&Build')
    
    self.connect( self, SIGNAL("CMDOUT"), self.cmd_out )
    
    Assemble = QAction('Assemble', self)  # F5
    Assemble.setShortcut('F5')
    Assemble.setStatusTip('Assemble files')
    Assemble.triggered.connect(self.Assemble)
    
    Run = QAction('Run', self)  # F6
    Run.setShortcut('F6')
    Run.setStatusTip('Open emulator')
    Run.triggered.connect(self.RunEmulator)

    Debug = QAction('Debug', self)  # F7
    Debug.setStatusTip('Open debugger')
    Debug.setShortcut('F7')
    Debug.triggered.connect(self.Debug)  
    
    BuildRun = QAction('Assemble and Run', self)    # CTRL+F6
    BuildRun.setStatusTip('Assemble files and Run emulator')
    BuildRun.setShortcut('Ctrl+F6')
    BuildRun.triggered.connect(self.Run_Assemble)  

    DebugRun = QAction('Assemble and Debug', self)  # CTRL+F7
    DebugRun.setStatusTip('Assemble files and open Debugger')
    DebugRun.setShortcut('Ctrl+F7')
    DebugRun.triggered.connect(lambda: self.Run_Assemble(1))

    build_menu.addAction(Assemble)
    build_menu.addAction(Run)
    build_menu.addAction(Debug)
    build_menu.addAction(BuildRun)
    build_menu.addAction(DebugRun)
    
    # create template menu
    self.template_menu = self.menubar.addMenu('&Templates')
    self.template_menu.aboutToShow.connect(self.TemplatesSetup)
    
    # create options menu
    format = self.menubar.addMenu('&Options')
    
    self.taxEnable = QAction('Enable Syntax Highlighting', self)
    self.taxEnable.setStatusTip('Enable/Disable syntax highlighting')
    self.taxEnable.setCheckable(True)
    self.taxEnable.setChecked(includes.cfg.getBool("SyntaxHighlighting", "On"))
    self.taxEnable.triggered.connect(self.SyntaxOnOff)
    
    self.tabEnable = QAction('Spaces Instead of Tabs', self)
    self.tabEnable.setStatusTip('Use Spaces Instead of Tabs')
    self.tabEnable.setCheckable(True)
    self.tabEnable.setChecked(includes.cfg.getBool("Font", "Tab"))
    self.tabEnable.triggered.connect(self.TabOnOff)
    
    self.syntaxAction = QAction('Syntax Highlighting', self)
    self.syntaxAction.setStatusTip('Change syntax highlighting')
    self.syntaxAction.triggered.connect(self.EditSyntax)
    
    fontAction = QAction('Font', self)
    fontAction.setStatusTip('Change font')
    fontAction.triggered.connect(self.ChangeFont)
    
    self.CMD = QAction('CMD Prompt', self)
    self.CMD.setStatusTip('Enable/Disable command prompt')
    self.CMD.setCheckable(True)
    self.CMD.setChecked(includes.cfg.getBool("Win", "CMD"))
    self.CMD.triggered.connect(self.cmdeor)
    self.CMD.setShortcut('F8')
    
    SetAction = QAction('Build Settings', self)
    SetAction.setStatusTip('Change Build Settings')
    SetAction.triggered.connect(self.Settings)
    
    format.addAction(self.tabEnable)
    format.addAction(self.taxEnable)
    format.addAction(self.syntaxAction)
    format.addSeparator()
    format.addAction(fontAction)
    format.addAction(self.CMD)
    format.addAction(SetAction)
    
    if includes.cfg.getBool("SyntaxHighlighting", "On"):  # check from config file if syntax highlighting is on
      self.syntaxAction.setDisabled(0)  # enable syntax edit window
    else:
      self.syntaxAction.setDisabled(1)  # disable syntax edit window
    
    self.cmdprompt()
   
    # create main window
    
    self.resize(includes.cfg.getInt("Win", "XSize"), includes.cfg.getInt("Win", "YSize"))
    self.setWindowTitle('ASM Development Environment')
    self.setWindowIcon(QIcon('includes/imgs/icon.png'))        
    self.show()
    
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    if not os.path.isfile("config.ini"):
      QMessageBox.warning(self, "Warning", "config file not found!");
  
      # get command line arguments
    if len(sys.argv) > 0:
      i = 1
      files = []          
      while i != len(sys.argv):      
      
        if sys.argv[i].lower().endswith('.adeproj'):
          self.openProject(sys.argv[i])
        else:
          files.append( sys.argv[i] ) # make a list out of the arguments (skipping the first one)
          
        i += 1
      self.openFile( files )  # open file(s)
    
    self.statusBar().showMessage('Ready')
      
##
######################################

######################################
##
## Syntax stuff

  def SyntaxOnOff(self):
    
    cfgfile = open("config.ini",'w')  # open config file for writing
    
    try:
      Config.add_section('SyntaxHighlighting')
    except:
      pass
    
    On = 1
    if self.taxEnable.isChecked():
      Config.set('SyntaxHighlighting','On', "1")  # set syntax highlighting on in config
      self.syntaxAction.setDisabled(0)  # enable syntax edit window
    else:
      Config.set('SyntaxHighlighting','On', "0")  # set syntax highlighting off in config
      self.syntaxAction.setDisabled(1)  # disable syntax edit window
      On = 0
     
    Config.write(cfgfile)
    cfgfile.close()
    
    numb = len(text)  # get text areas
    i = 0
    while i != numb:
      includes.SyntaxHighlighting.Highlighter(text[i], On ) # loop through each one and enable/disable syntax highliting to text area
      i += 1
          
  def EditSyntax(self):
    self.w = includes.SyntaxEditWindow.MainWindow(text, Config) # display syntax edit window and pass text boxes so we can update them
    self.w.show()

##
######################################

######################################
## Project

  def FileInit(self):
    if self.PROJ != "":
      self.CloseProj.setVisible(1)
    else:
      self.CloseProj.setVisible(0)
      
  def newProject(self):
      
    filename = QFileDialog.getSaveFileName(self, 'New Project', '', "ADE Project File (*.adeproj)")
    if filename == "": return # if we don't choose a file to save as; return
    
    self.Settings()

    self.PROJ = str(filename) # QString -> string
    self.setWindowTitle(os.path.basename(self.PROJ))
  
  def openProject(self, file=""):
    
    if file == "":
      filename = QFileDialog.getOpenFileName(self, 'Open Project', '', "ADE Project File (*.adeproj)") # open "open file dialog"
      if filename == "": return # if we didn't choose a file to open; return
    else:
      filename = file
     
    if self.closeAll() == 0:
      return
      
    try:
      f = open(filename)
      lines = f.readlines()
      f.close()
    except:
      QMessageBox.critical(self, "Error", "Could not open [" + filename + "] !");
      return
    
    try:
      a = 0
      while lines[a] != "[CMDS]\n":
        string = lines[a].split(' = ');
        if string[0] == "emulator":
          self.Emulator = string[1].rstrip('\n')
        elif string[0] == "debugger":
          self.Debugger = string[1].rstrip('\n')
        elif string[0] == "rom":
          self.ROM = string[1].rstrip('\n')
        elif string[0] == "maps":
          self.Maps = string[1].rstrip('\n')
          
        a += 1
      
      self.CMDS = ""
      
      a += 1
      while lines[a] != "[Files]\n":
        if lines[a] != "\n":
          self.CMDS += lines[a]
        a += 1
     
      
      while a+1 < len(lines):
        a += 1
        if lines[a] != "\n":
          if lines[a] == "Untitled\n":
            self.newTab()
          else:
            self.openFile( [lines[a].rstrip('\n')] )
        
      
      self.PROJ = str(filename)
      self.setWindowTitle(os.path.basename(self.PROJ))
    except:
      QMessageBox.critical(self, "Error", "Project format error.");
      
  def closeProject(self):
    self.saveProject()
    if self.closeAll() == 0:
      return
    self.PROJ = ""
    self.setWindowTitle('ASM Development Environment')
  
  def saveProject(self):
    if self.PROJ != "":
      f = open(self.PROJ, 'w')
      f.write("emulator = " + self.Emulator + "\n")
      f.write("debugger = " +self.Debugger + "\n")
      f.write("rom = " + self.ROM + "\n")
      f.write("maps = " + self.Maps + "\n")
      f.write("[CMDS]\n")
      f.write(self.CMDS + "\n")
      f.write("[Files]\n")
      
      a = 0
      while a != len(text):
        try:
          f.write(savepaths[a] + "\n")
        except:
          f.write("Untitled\n")
        a += 1
      f.close()             
##
######################################

######################################
## Find/Replace/Goto
  
  def FindDialog(self):
  
    try:
      self.w_2.close()
    except:
      pass
      
    self.w_2 = includes.CtrlF.MainWindow(self) # display find text window
    self.w_2.show()
      
  def ReplaceDialog(self):
  
    try:
      self.w_2.close()
    except:
      pass
      
    self.w_2 = includes.CtrlH.MainWindow(self) # display find/replace text window
    self.w_2.show()

  def GotoDialog(self):
  
    try:
      if self.w_3:
        return
    except:
      pass
      
    self.w_3 = includes.CtrlG.MainWindow(self) # display goto window
    self.w_3.show()
  
  def Goto(self, line):
  
    numb = self.tab_widget.currentIndex() # get active tab number
    
    if numb < 0:
      return
    
    try:
      lineNumber = int(line.text())
    except:
      line.selectAll()
      return
      
    cursor = text[numb].textCursor();
    cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
    cursor.movePosition(QTextCursor.Down, QTextCursor.MoveAnchor, lineNumber-1)
    text[numb].setTextCursor(cursor);
    text[numb].setFocus();
  
  def FindNext(self):
    
    if not self.FindText(0, 0):
      if QMessageBox.warning(self, 'Warning', "The text could not be found!\n\nSearch from begining?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
        if not self.FindText(0, 1):
          QMessageBox.warning(self, 'Warning', "The text could not be found!")

  def FindPrev(self):
    
    if not self.FindText(1, 0):
      if QMessageBox.warning(self, 'Warning', "The text could not be found!\n\nSearch from end?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
        if not self.FindText(1, 2):
          QMessageBox.warning(self, 'Warning', "The text could not be found!")

  def Replace(self):
    if self.word:
      self.ReplaceText()
      self.FindNext()
    else:
      self.ReplaceDialog()
    
  def ReplaceText(self):
  
    numb = self.tab_widget.currentIndex() # get active tab number
    
    if numb < 0:
      return
      
    if not text[numb].textCursor().hasSelection():
      return
    
    if self.regex:
      try:
        replace = re.sub(r"" + str(self.word), r"" + str(self.replace), str(text[numb].textCursor().selectedText()))
      except:
        replace = self.replace
    else:
      replace = self.replace
      
    text[numb].textCursor().insertText(replace)
    return 1
    
  def FindText(self, backwards, start = 0):
    
    numb = self.tab_widget.currentIndex() # get active tab number
    
    if numb < 0:
      return 1
    
    flags = QTextDocument.FindFlags()
    
    if backwards:
      flags |= QTextDocument.FindBackward
    if self.case:
      flags |= QTextDocument.FindCaseSensitively
    if self.whole:
      flags |= QTextDocument.FindWholeWords
    if self.regex:
      search = QRegExp(self.word)
    else:
      search = self.word
    
    if start == 1:
      c = text[numb].textCursor()
      c.movePosition(
                  QTextCursor.Start, QTextCursor.MoveAnchor)
      text[numb].setTextCursor(c)
    elif start == 2:
      c = text[numb].textCursor()
      c.movePosition(
                  QTextCursor.End, QTextCursor.MoveAnchor)
      text[numb].setTextCursor(c)
    
    c = text[numb].document().find(search, text[numb].textCursor(), flags)
    
    if not c.isNull():
      text[numb].setTextCursor(c)
      text[numb].setFocus()
      return 1
    
    return

##
######################################

######################################
##
## Tab stuff

  def closeAll(self):
    
    # loop through all text boxes
    while len(text) != 0:
      if self.removeTab(len(text)-1) == 24:
        return 0 
    return 1
        
  def removeTab(self, index):
    
    tab_name = str(self.tab_widget.tabText(index))  # get the tab name
    self.tab_widget.setCurrentIndex(index)  # set the current tab index to the one we want to close out
    if re.search(r'^\* ', tab_name): # if the file is unsaved...
      # ...ask if we want to save
      reply = QMessageBox.warning(self, 'Warning', 
                       "\"" + re.sub(r'^\* ', '', tab_name) + "\" was not saved.\n\nWould you like to save now?", QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel)
      if reply == QMessageBox.Yes:
        self.saveFile(0, index)
      elif reply != QMessageBox.No:
        return 24
    
    
    # delete current tab and reorganize dicts
    text[index].deleteLater()
    del text[index] # text box
    
    last = -1
    for key in sorted(text):
      if last+1 != key:
        text[key-1] = text[key]
        del text[key]
      last += 1
    
    try:
      del savepaths[index]
      last = -1
      for key in sorted(savepaths):
        if last+1 != key:
          savepaths[key-1] = savepaths[key]
          del savepaths[key]
        last += 1
    except:
      pass
    
    widget = self.tab_widget.currentWidget()
    self.tab_widget.removeTab(index)  # remove tab
    widget.deleteLater()
    del widget
  
  def newTab(self, TabName=">Untitled.asm"):
    
    numb = len(text)  # get number of tabs
    
    # create tab
    self.tab_widget.addTab(includes.TextEdit.TextWidget(self, text), TabName)

    # set font
    font = QFont()
    font.fromString(QString(includes.cfg.get("Font", "Font")))
    text[numb].setFont(font)
    
    # focus on the new tab
    self.tab_widget.setCurrentIndex(numb)
    
    return numb

##
######################################

######################################
##
## CMD

  def Run_Assemble(self, debug=0):
    self.Assemble()
    while self.ASDone != 0:
          pass
    if debug == 1:
      self.Debug()
    else:
      self.RunEmulator()
    
  def Debug(self):
    a = self.Debugger
    b = self.ROM
    if not a:
      a = includes.cfg.get("CMD", "Debugger")
      if not a:
        QMessageBox.critical(self, "Error", "No debugger set.");
        return
    if not b:
      b = includes.cfg.get("CMD", "ROM")
    
    subprocess.Popen(str("\"" + a + "\" " + "\"" + b + "\""), shell=True)
    
  def RunEmulator(self):
    a = self.Emulator
    b = self.ROM
    if not a:
      a = includes.cfg.get("CMD", "Emulator")
      if not a:
        QMessageBox.critical(self, "Error", "No emulator set.");
        return
    if not b:
      b = includes.cfg.get("CMD", "ROM")
    
    subprocess.Popen(str("\"" + a + "\" " + "\"" + b + "\""), shell=True)
    
      
  def Assemble(self):    
    if not self.CMDS:
      a = includes.cfg.get("CMD", "CMDS").split('\n')
    else:
      a = self.CMDS.split('\n')

    if a == ['']:
      QMessageBox.critical(self, "Error", "No command line arguments set.");
      return
    
    self.ASDone = len(a)
    for b in a:
      self.cmd_enter(b)
    
  def Settings(self):
  
    try:
      self.w.close()
    except:
      pass
      
    self.w = includes.Settings.MainWindow(self, Config) # display find text window
    self.w.exec_()
    
  def cmdeor(self):
  
    cfgfile = open("config.ini",'w')  # open config file for writing
    
    try:
      Config.add_section('Win')
    except:
      pass
    
    if not self.CMD.isChecked():
      self.dockWidget.setVisible(False)
      self.textEdit.setVisible(False)
      self.ComboBox.setVisible(False)
      Config.set('Win','CMD', False)
    else:
      self.dockWidget.setVisible(True)
      self.textEdit.setVisible(True)
      self.ComboBox.setVisible(True)
      Config.set('Win','CMD', True)
    
    Config.write(cfgfile)
    cfgfile.close()
  
  def cmd_out(self, text):
    self.textEdit.append( text )
    
  def cmd_enter(self, text):
  
    self.textEdit.clear()
    cmd = str(text)
    
    import threading
    
    def runInThread(self, cmd):
        while self.busy == 1:
          pass
        self.busy = 1
        p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        self.emit(SIGNAL('CMDOUT'), out + err)
        self.busy = 0
        self.ASDone -= 1
        return
        
    thread = threading.Thread(target=runInThread, args=(self, cmd))    
    thread.start()
    
  def cmdprompt(self):
    # set inactive higlighted text color
    palette = QPalette()
    brush = QBrush(QColor(51, 153, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
    self.setPalette(palette)
    
    self.dockWidget = QDockWidget(self)
    self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)

    self.textEdit = QTextEdit()
    self.textEdit.setGeometry(QRect(40, 10, 104, 71))
    self.textEdit.setObjectName("textEdit")
    self.textEdit.setReadOnly(True)
    
    palette = QPalette()
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Active, QPalette.Light, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Active, QPalette.Text, brush)
    brush = QBrush(QColor(0, 0, 0))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Active, QPalette.Base, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
    brush = QBrush(QColor(0, 0, 0))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
    brush = QBrush(QColor(240, 240, 240))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
    self.textEdit.setPalette(palette)
    font = QFont()
    font.setFamily("Lucida Console")
    self.textEdit.setFont(font)

    self.dockWidget.setWidget(self.textEdit)
    
    self.addDockWidget(Qt.DockWidgetArea(8), self.dockWidget)

    #global LineEdit
    self.ComboBox = QComboBox(self)
    self.ComboBox.setEditable(True)
    self.ComboBox.activated['QString'].connect(self.cmd_enter)
    
    palette = QPalette()
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Active, QPalette.Text, brush)
    brush = QBrush(QColor(0, 0, 0))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Active, QPalette.Base, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
    brush = QBrush(QColor(0, 0, 0))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
    brush = QBrush(QColor(255, 255, 255))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
    brush = QBrush(QColor(0, 0, 0))
    brush.setStyle(Qt.SolidPattern)
    palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
    self.ComboBox.setPalette(palette)
    font = QFont()
    font.setFamily("Lucida Console")
    self.ComboBox.setFont(font)
    
    self.dockWidget.setVisible( includes.cfg.getBool("Win", "CMD") )
    self.textEdit.setVisible( includes.cfg.getBool("Win", "CMD") )
    self.ComboBox.setVisible( includes.cfg.getBool("Win", "CMD") )
    
##
######################################

######################################
##
## Event stuff
  
  def TabOnOff(self):
    
    cfgfile = open("config.ini",'w')  # open config file for writing
    
    try:
      Config.add_section('Font')
    except:
      pass
    
    if self.tabEnable.isChecked():
      Config.set('Font','Tab', "1")  # set syntax highlighting on in config
    else:
      Config.set('Font','Tab', "0")  # set syntax highlighting off in config
     
    Config.write(cfgfile)
    cfgfile.close()
    
  def ChangeFont(self):
    
    font, ok = QFontDialog.getFont()
    
    numb = len(text)  # get number of tabs
    
    if ok and numb >= 0:    
        i = 0
        while i != numb:
                
          text[i].setFont(font)
          i += 1
        
        cfgfile = open("config.ini",'w')  # open config file for writing
        
        try:
          Config.add_section('Font')
        except:
          pass
        
        Config.set('Font','Font', QFont.toString(font))  # set font in config
         
        Config.write(cfgfile)
        cfgfile.close()
  
  def resizeEvent(self, event=None):
    #widget.move(x, y)
    self.ComboBox.move(0, (self.height() - self.ComboBox.height()) - 20)
    #if you want the widgets width equal to window width:
    self.ComboBox.resize(self.width(), 20)
        
  def closeEvent(self, event):    
      
      self.saveProject()
        
      if self.saveAll(1) == 1:  # check for any unsaved files and ask if we want to save them
        event.ignore()  # if we hit cancel don't close out

      cfgfile = open("config.ini",'w')  # open config file for writing
      
      try:
        Config.add_section('Win')
      except:
        pass
      
      Config.set('Win','XSize', self.width())  # set font in config
      Config.set('Win','YSize', self.height())
      
      Config.write(cfgfile)
      cfgfile.close()
      
  def SelectAll(self):
    numb = self.tab_widget.currentIndex() # get active tab number
    text[numb].selectAll()
    
  def EditInit(self):
    numb = self.tab_widget.currentIndex() # get active tab number
    
    if numb < 0:
      self.UndoAction.setDisabled(1)
      self.RedoAction.setDisabled(1)
      self.CutAction.setDisabled(1)
      self.CopyAction.setDisabled(1)
      self.PasteAction.setDisabled(1)
      self.SelectAllAction.setDisabled(1)
      self.FindAction.setDisabled(1)
      self.FindNAction.setDisabled(1)
      self.FindPAction.setDisabled(1)
      self.ReplaceAction.setDisabled(1)
      self.ReplaceNAction.setDisabled(1)
      self.GotoAction.setDisabled(1)
      return
      
    self.SelectAllAction.setDisabled(0)
    self.FindAction.setDisabled(0)
    self.FindNAction.setDisabled(0)
    self.FindPAction.setDisabled(0)
    self.ReplaceAction.setDisabled(0)
    self.ReplaceNAction.setDisabled(0)
    self.GotoAction.setDisabled(0)
    
    if text[numb].canPaste():
      self.PasteAction.setDisabled(0)
    else:
      self.PasteAction.setDisabled(1)
      
  def Paste(self):
    numb = self.tab_widget.currentIndex() # get active tab number
    text[numb].paste()
    
  def CopyAvailable(self, bool):
    if bool:
      self.CutAction.setDisabled(0)
      self.CopyAction.setDisabled(0)
    else:
      self.CutAction.setDisabled(1)
      self.CopyAction.setDisabled(1)
  
  def Copy(self):
    numb = self.tab_widget.currentIndex() # get active tab number
    text[numb].copy()
    
  def Cut(self):
    numb = self.tab_widget.currentIndex() # get active tab number
    text[numb].cut()
    
  def UndoAvailable(self, bool):
    if bool:
      self.UndoAction.setDisabled(0)
    else:
      numb = self.tab_widget.currentIndex() # get active tab number  
      if re.search(r'^\* ', str(self.tab_widget.tabText(numb))):  # if we already have a '*' in front of the name skip doing it again
        self.tab_widget.setTabText(numb, re.sub(r'^\* ', '', str(self.tab_widget.tabText(numb))))
      self.UndoAction.setDisabled(1)
  
  def Undo(self):
    numb = self.tab_widget.currentIndex() # get active tab number  
    text[numb].undo()
    
  def RedoAvailable(self, bool):
    if bool:
      self.RedoAction.setDisabled(0)
    else:
      self.RedoAction.setDisabled(1)
      
  def Redo(self):
    numb = self.tab_widget.currentIndex() # get active tab number      
    text[numb].redo()
    
  def cursorPositionChanged(self):
    
    numb = self.tab_widget.currentIndex() # get active tab number
      
    if numb > -1:
      # get current line
      cursor = text[numb].textCursor();
      y = cursor.blockNumber() + 1;
      x = cursor.columnNumber() + 1;
      
      # get number of lines in file
      line_count = 0
      contents_y = text[numb].verticalScrollBar().value()
      page_bottom = contents_y + text[numb].viewport().height()
              
      # Iterate over all text blocks in the document.
      block = text[numb].document().begin()
      while block.isValid():
          line_count += 1

          # The top left position of the block in the document
          position = text[numb].document().documentLayout().blockBoundingRect(block).topLeft()

          # Check if the position of the block is out side of the visible
          # area.
          if position.y() > page_bottom:
              break

          block = block.next()
                  
      self.statusBar().showMessage("Line " + str(y) + " : " + str(line_count) + " Pos " + str(x))

  def textChanged(self):    
    # when the text has been changed...
    numb = self.tab_widget.currentIndex() # get active tab number 
    
    if re.search(r'^>', str(self.tab_widget.tabText(numb))):   # if this is a new tab...
       self.tab_widget.setTabText(numb, re.sub(r'^>', '', str(self.tab_widget.tabText(numb))) )  #... remove the '^' and carry on
    elif not re.search(r'^\* ', str(self.tab_widget.tabText(numb))):  # if we already have a '*' in front of the name skip doing it again
      self.tab_widget.setTabText(numb, "* " + self.tab_widget.tabText(numb))
    #if not re.search(r'^\* ', str(self.tab_widget.tabText(numb))):  # if we already have a '*' in front of the name skip doing it again
    #  self.tab_widget.setTabText(numb, "* " + self.tab_widget.tabText(numb))        
                
  def saveAll(self, exit = 0):
    numb = len(text)  # get all text boxes
    
    if numb == 0 and exit == 0:
      # if there is nothing to save return
      self.statusBar().showMessage("Nothing to save!"); return 0
    
    # loop through all text boxes
    i = 0
    while i != numb:
      tab_name = str(self.tab_widget.tabText(i))  # get the current text box tab's name
      if re.search(r'^\* ', tab_name):  # if it is not saved...
      
        if exit == 1: # ... check if this is the exit event...
        
          # ask if we want to save
          reply = QMessageBox.warning(self, 'Warning',
          "\"" + re.sub(r'^\* ', '', tab_name) + "\" has not been saved.\n\nDo you want to save now?", QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel)
          
          if reply == QMessageBox.No:
              i += 1
              continue
          elif reply == QMessageBox.Cancel:
              return 1
          
        self.saveFile(0, i) # ... save current file
      i += 1
    return 0
    
  def saveFile(self, As=1, numb = None):
    
    if numb is None:
      numb = self.tab_widget.currentIndex() # if we weren't given a tab then use the current active tab
    
    # however if there are no tabs open retrun
    if numb < 0:
      self.statusBar().showMessage("Nothing to save!"); return
    
    # if we clicked 'Save As' or we did not save before, open Save File Dialog
    if As == 1 or not numb in savepaths:
      # open "save dialog"
      filename = QFileDialog.getSaveFileName(self, 'Save File', '', "Assembly file (*.asm);;All Files (*.*)")
      if filename == "": return # if we don't choose a file to save as; return
      savepaths[numb] = str(filename) # add path to dict
    else:
      # otherwise take the path from the dict
      filename = savepaths[numb]
      
    self.tab_widget.setTabText(numb, os.path.basename(str(filename))) # change tab name to filename
    
    try:  
      # write data out
      f = open(filename, 'w')
      filedata = text[numb].toPlainText()
      f.write(filedata)
      f.close()
    except:
      QMessageBox.critical(self, "Error", "Could not save [" + filename + "]");
      
  def openFile(self, filenames=None):
  
    if filenames is None:
      # if we weren't given files to open ask for one
      filenames = QFileDialog.getOpenFileNames(self, 'Open File', '', "Assembly file (*.asm);;All Files (*.*)") # open "open file dialog"
      if filenames == "": return # if we didn't choose a file to open; return
    
    # open files and write data to tab
    for filename in filenames:
      try:
        f = open(filename, 'r')
        filedata = f.read()
        path = str(filename)
        filename = os.path.basename(str(filename))    # QString -> string
        numb = self.newTab( ">" + filename ) # > tells us it is a brand new tab... kind of hacky
        text[numb].setText(filedata)   # create tab with the file name and write the data
        savepaths[numb] = path # add path to dict
        f.close()
      except:
        QMessageBox.critical(self, "Error", "Could not open \"" + filename + "\"");
        return 24
    
  def TemplateInsert(self, path):
    numb = self.tab_widget.currentIndex()   # get currently selected tab
    
    try:
      f = open(path, 'r')   # open file
      filedata = f.read()
      
      if numb < 0:
        text[self.newTab()].setText(filedata)   # if we don't have a tab open create a new one with the template
      else:
        text[numb].insertPlainText(filedata)   # otherwise insert the template
      f.close()
    except:
      QMessageBox.critical(self, "Error", "Could not open template!");

##
######################################

######################################
##
## Create template menu

  def TemplatesSetup(self):
    
    # erase menu contents
    self.template_menu.clear()
    
    # check if templates folder exists
    if os.path.exists('templates/') is False:
      temp = QAction('Can not find templates folder...', self)
      temp.setDisabled (1)
      self.template_menu.addAction(temp)
      return
    
    menus = {'templates': self.template_menu}
    
    # create menu
    for dirpath, dirnames, filenames in os.walk('templates'):
        current = menus[dirpath]
        for dn in dirnames:
            menus[os.path.join(dirpath, dn)] = current.addMenu(dn)
        for fn in filenames:
            temp = QAction(os.path.splitext(fn)[0], self)
            self.connect(temp, SIGNAL("triggered()"), lambda path=(dirpath + "/" + fn): self.TemplateInsert(path))
            current.addAction( temp )


##
######################################

def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

