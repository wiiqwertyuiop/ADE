'''
The MIT License

Copyright (c) 2009 John Schember <john@nachtimwald.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE
'''

####################
## Most of this isn't my code
## it is a text edit widget with line numbers
####################

import re
import cfg
import SyntaxHighlighting
import Defs

from PyQt4.Qt import *
    
class TextEdit(QTextEdit):
  def __init__(self, main):
    QTextEdit.__init__(self)
    self.main = main
    self.setMouseTracking(1)

  def keyPressEvent(self, event):
    
    if event.key() == Qt.Key_Tab and self.main.tabEnable.isChecked():
      self.insertPlainText("    ")
      return
      
    return QTextEdit.keyPressEvent(self, event)
    
  def mouseMoveEvent(self, event):

    if event.buttons() == Qt.NoButton:
        
        # get the word our cursor is over
        textCursor = self.cursorForPosition(event.pos())
        textCursor.select(QTextCursor.WordUnderCursor)   
        
        #textCursor.setPosition(textCursor.selectionStart())
        #textCursor.setPosition(textCursor.selectionStart()-1, QTextCursor.KeepAnchor)
        
        word = textCursor.selectedText()     
        
        start = textCursor.selectionStart()
        end = textCursor.selectionEnd()
        
        x = self.cursorRect(textCursor).x()
        y = self.cursorRect(textCursor).y()
        
        i = 0
        while not textCursor.atBlockEnd():
          textCursor.setPosition(end+i, QTextCursor.KeepAnchor)
          if not re.search( r'\s', textCursor.selectedText()):
            i += 1
          else:
            break
        
        word = textCursor.selectedText()    
        if re.search( r'\s', word): 
            word = word[:-1]
        
        i = 0
        while not textCursor.atBlockStart():
          textCursor.setPosition(start+i, QTextCursor.KeepAnchor)
          if not re.search( r'\s', textCursor.selectedText()):
            i -= 1
          else:
            break

        word = textCursor.selectedText() + word
        if re.search( r'\s', word):
            word = word[1:]
        
        # find the tooltip for this word if there is one        
        toolTipText = Defs.check(str(word), self.main)
        
        # i don't even know what I am doing here; it fixes a bug with the cursor
        Ysize = self.currentFont().pointSize()
        
        if x >= event.pos().x()+2 and y >= (event.pos().y()-5)-Ysize and toolTipText:
          QToolTip.showText(event.globalPos(), toolTipText)    
        else:
          QToolTip.hideText()
        
    return QTextEdit.mouseMoveEvent(self, event)
        

class TextWidget(QFrame):
 
    class NumberBar(QWidget):
 
        def __init__(self, *args):
            QWidget.__init__(self, *args)
            self.edit = None
            # This is used to update the width of the control.
            # It is the highest line that is currently visibile.
            self.highest_line = 0
 
        def setTextEdit(self, edit):
            self.edit = edit
 
        def update(self, *args):
            '''
            Updates the number bar to display the current set of numbers.
            Also, adjusts the width of the number bar if necessary.
            '''
            # The + 4 is used to compensate for the current line being bold.
            width = self.fontMetrics().width(str(self.highest_line)) + 10
            if self.width() != width:
                self.setFixedWidth(width)
            QWidget.update(self, *args)
 
        def paintEvent(self, event):            
            
            contents_y = self.edit.verticalScrollBar().value()
            page_bottom = contents_y + self.edit.viewport().height()
            font_metrics = self.fontMetrics()
            current_block = self.edit.document().findBlock(self.edit.textCursor().position())
        
            painter = QPainter(self)
           
            # made it so it shows a line dividing the line numbers from the main text file
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.width(), 0, self.width(), page_bottom)
            
            # give the line numbers a grey bg
            painter.setBrush(QColor(200, 200, 200))
            painter.drawRect(0, 0, self.width(), page_bottom+1)
            
            line_count = 0
            # Iterate over all text blocks in the document.
            block = self.edit.document().begin()
            while block.isValid():
                line_count += 1
 
                # The top left position of the block in the document
                position = self.edit.document().documentLayout().blockBoundingRect(block).topLeft()
 
                # Check if the position of the block is out side of the visible
                # area.
                if position.y() > page_bottom:
                    break
 
                # We want the line number for the selected line to be bold.
                bold = False
                if block == current_block:
                    bold = True
                    font = painter.font()
                    font.setBold(True)
                    painter.setFont(font)
 
                # Draw the line number right justified at the y position of the
                # line. 3 is a magic padding number. drawText(x, y, text).
                painter.drawText(self.width() - font_metrics.width(str(line_count)) - 7, round(position.y()) - contents_y + font_metrics.ascent(), str(line_count))
 
                # Remove the bold style if it was set previously.
                if bold:
                    font = painter.font()
                    font.setBold(False)
                    painter.setFont(font)
 
                block = block.next()
 
            self.highest_line = line_count
            
            painter.end()
 
            QWidget.paintEvent(self, event)            
 
    def __init__(self, main, text):
        QFrame.__init__(self)
 
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
 
        self.numb = len(text)  # get number of tabs
    
        text[self.numb] = TextEdit(main)
        text[self.numb].setFrameStyle(QFrame.NoFrame)
        text[self.numb].setAcceptRichText(False)
 
        if cfg.getBool("SyntaxHighlighting", "On"):
          SyntaxHighlighting.Highlighter(text[self.numb]) # add syntax highliting to text area
        
        self.number_bar = self.NumberBar()
        self.number_bar.setTextEdit(text[self.numb])
 
        hbox = QHBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setMargin(0)
        hbox.addWidget(self.number_bar)
        hbox.addWidget(text[self.numb])
 
        self.text = text
        
        text[self.numb].setUndoRedoEnabled(1) # enable undo/redo
        
        text[self.numb].installEventFilter(self)
        text[self.numb].viewport().installEventFilter(self)
                
        text[self.numb].textChanged.connect(main.textChanged)
        text[self.numb].cursorPositionChanged.connect(main.cursorPositionChanged)
        
        text[self.numb].undoAvailable.connect(main.UndoAvailable)
        text[self.numb].redoAvailable.connect(main.RedoAvailable)
        
        text[self.numb].copyAvailable.connect(main.CopyAvailable)
        
        metrics = text[self.numb].fontMetrics()
        text[self.numb].setTabStopWidth((8*7)-4);
        #text[self.numb].setTabStopWidth(12 * metrics.width(' '));
    
    def eventFilter(self, object, event):
        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        if self.numb not in self.text:
          return False
          
        if object in (self.text[self.numb], self.text[self.numb].viewport()):
            self.number_bar.update()
            return False
        try:
          return QFrame.eventFilter(object, event)
        except:
          return False
          
    #def getTextEdit(self):
    #    return self.TEXT[self.numb]