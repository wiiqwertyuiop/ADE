# Format:
# [what to look for][tab][anything else]

import re
import cfg
import SNES
    
def check(word, main):
  
  try:
    if re.match( r'^\#', word):
      type = 0
      
      if re.match( r'^\#%', word):
        word = word[2:]
        type = 1
      elif re.match( r'^\#\$', word):
        word = word[2:]
        type = 2
      else:
        word = word[1:]
        
      return const(word, type)
    elif re.match( r'^\$', word):
      
      word = word[1:] # remove '$'
      
      # convert it to hex
      numb = int(str(word), 16)
      
      # if it is see if we have a map set
      map = main.Maps
    
      if map == "": # if we don't try the defualt map
        map = cfg.get("CMD", "Maps")
      
      # if we don't have a map set return
      if map == "":
        return

      return addr(map, numb)
    else:
      return opcode(word)
  except:
    return
    
def const(numb, type):
  try:
    if type == 0:
      return "Dec: %s\nHex: $%04X\nBinary: %%%s" % (str(numb), int(str(numb)), bin(int(str(numb)))[2:])
    elif type == 1:
      return "Binary: %%%s\nDec: %i\nHex: $%04X" % (str(numb), int(str(numb), 2), int(str(numb), 2))
    else:
      return "Hex: $%04X\nDec: %i\nBinary: %%%s" % (int(str(numb), 16), int(str(numb), 16), bin(int(str(numb), 16))[2:])
  except:
    return
    
def addr(map, numb):
  
  # read map
  try:
    f = open(map)
    lines = f.readlines()
    f.close()
  except:
    return "[" + map + "] file not found."
  
  
  if numb <= 8191:  # if $0000-$1FFF assume RAM
    numb += 0x7E0000
  # Anything else assume ROM
  
  # loop through file
  a = 0
  for line in lines:
    # find addr
    if re.match( r'^\$[0-9A-F][0-9A-F]:[0-9A-F]+?\t', line):
    
      first = int(re.sub(r'^\$([0-9A-F][0-9A-F]):([0-9A-F]+?\t).+$', r'\1\2', line, re.I), 16)
      much = re.sub(r'^\$[0-9A-F][0-9A-F]:[0-9A-F]+?\t(.+?)\s.+$', r'\1', line, re.I)
      much = int(re.sub(r',', r'', much, re.I))-1
      end = first+much
      
      out = line
      i = a+1
      while i < len(lines):
        if re.match( r'^\$\S+?\t', lines[i]):
          break
        out += lines[i]
        i += 1
        
      if numb == first:        
        return out[:-1]
      elif numb >= first and numb <= end:
        string = re.sub(r'^(\$[0-9A-F][0-9A-F]):([0-9A-F]+?)\t.+$', r'\1\2', line, re.I)
        return "Address not found showing " + string[:-1] + " instead:\n" + out[:-1]
    a += 1  

def opcode(word):

  try:
    f = open('Maps/Opcodes.txt')
    lines = f.readlines()
    f.close()
  except:
    return "[Maps/Opcodes.txt] file not found."
    
  a = 0
  for line in lines:
    if re.match( r'^\S+?\t', line):
      words = line.split('	')
      if str(words[0]).lower() == str(word).lower():
        text = line
        i = a
        while i < len(lines):
          if not re.match( r'^\S+?\t', lines[i]):
            text += lines[i]
          i += 1
        return text.strip()
    a += 1
  