####################
## Syntax highlighting function
####################

import cfg
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from ADE import Config

class Highlighter( QSyntaxHighlighter ):

    def __init__(self, parent=None, On=1):
      super(Highlighter, self).__init__(parent)
      
      self.highlightingRules = []
      
      if not On:
        return
      
      # opcodes
      opcodes = QTextCharFormat()
      highlight = cfg.readList('SyntaxHighlighting', 'Opcodes')
      if highlight != ['']:
        color = QColor(cfg.getInt('SyntaxHighlighting', 'opR'),
          cfg.getInt('SyntaxHighlighting', 'opG'),
          cfg.getInt('SyntaxHighlighting', 'opB'))      
        brush = QBrush( color, Qt.SolidPattern )
        opcodes.setForeground( brush )
        
        if cfg.getBool('SyntaxHighlighting', 'opBold'):
          opcodes.setFontWeight( QFont.Bold )
        if cfg.getBool('SyntaxHighlighting', 'opUnderline'):
          opcodes.setFontUnderline(True)
        if cfg.getBool('SyntaxHighlighting', 'opItalic'):
          opcodes.setFontItalic(True)
                                         
        search = QStringList( highlight )
        
        self.highlightingRules = [(QRegExp("\\b" + pattern + "\\b", Qt.CaseInsensitive), opcodes)
                  for pattern in search]
      
      # key words
      keywords = QTextCharFormat()
      highlight = cfg.readList('SyntaxHighlighting', 'Keywords')
      if highlight != ['']:
        color = QColor(cfg.getInt('SyntaxHighlighting', 'keyR'),
          cfg.getInt('SyntaxHighlighting', 'keyG'),
          cfg.getInt('SyntaxHighlighting', 'keyB'))      
        brush = QBrush( color, Qt.SolidPattern )
        keywords.setForeground( brush )
        
        if cfg.getBool('SyntaxHighlighting', 'keyBold'):
          keywords.setFontWeight( QFont.Bold )
        if cfg.getBool('SyntaxHighlighting', 'keyUnderline'):
          keywords.setFontUnderline(True)
        if cfg.getBool('SyntaxHighlighting', 'keyItalic'):
          keywords.setFontItalic(True)
                                         
        search = QStringList( highlight )
                                   
        for pattern in search:
          self.highlightingRules.append( (QRegExp("\\b" + pattern + "\\b", Qt.CaseInsensitive), keywords) )

      # comment
      comment = QTextCharFormat()
      color = QColor(cfg.getInt('SyntaxHighlighting', 'cmntR'),
        cfg.getInt('SyntaxHighlighting', 'cmntG'),
        cfg.getInt('SyntaxHighlighting', 'cmntB')) 
        
      brush = QBrush( color, Qt.SolidPattern )
      comment.setForeground( brush )
      
      if cfg.getBool('SyntaxHighlighting', 'cmntBold'):
        comment.setFontWeight( QFont.Bold )
      if cfg.getBool('SyntaxHighlighting', 'cmntUnderline'):
        comment.setFontUnderline(True)
      if cfg.getBool('SyntaxHighlighting', 'cmntItalic'):
        comment.setFontItalic(True)
        
      self.highlightingRules.append( (QRegExp( ";[^\n]*" ), comment) )
      
      # addr
      address = QTextCharFormat()
      
      color = QColor(cfg.getInt('SyntaxHighlighting', 'addrR'),
        cfg.getInt('SyntaxHighlighting', 'addrG'),
        cfg.getInt('SyntaxHighlighting', 'addrB')) 
        
      brush = QBrush( color, Qt.SolidPattern )
      
      address.setForeground( brush )
      
      if cfg.getBool('SyntaxHighlighting', 'addrBold'):
        address.setFontWeight( QFont.Bold )
      if cfg.getBool('SyntaxHighlighting', 'addrUnderline'):
        address.setFontUnderline(True)
      if cfg.getBool('SyntaxHighlighting', 'addrItalic'):
        address.setFontItalic(True)
        
      self.highlightingRules.append( (QRegExp( "\\b\$[0-9A-F]+", Qt.CaseInsensitive ), address) )
   
      # labels
      labels = QTextCharFormat()
      
      color = QColor(cfg.getInt('SyntaxHighlighting', 'lblR'),
        cfg.getInt('SyntaxHighlighting', 'lblG'),
        cfg.getInt('SyntaxHighlighting', 'lblB')) 
        
      brush = QBrush( color, Qt.SolidPattern )
      
      labels.setForeground( brush )
      
      if cfg.getBool('SyntaxHighlighting', 'lblBold'):
        labels.setFontWeight( QFont.Bold )
      if cfg.getBool('SyntaxHighlighting', 'lblUnderline'):
        labels.setFontUnderline(True)
      if cfg.getBool('SyntaxHighlighting', 'lblItalic'):
        labels.setFontItalic(True)
        
      self.highlightingRules.append( (QRegExp( "\S+:", Qt.CaseInsensitive ), labels) )
      self.highlightingRules.append( (QRegExp( "[.!]\S+", Qt.CaseInsensitive ), labels) )

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)