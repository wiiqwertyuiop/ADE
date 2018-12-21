####################
## Helpers for reading cfg file data
####################

from ADE import Config

def readList(section, name):
  try:
    #Config.read("config.ini")
    list = Config.get(section, name)
    return list.split('\n')
  except:
    return []

def get(section, name):
  try:
    #Config.read("config.ini")
    return Config.get(section, name)
  except:
    return ""

def getInt(section, name):
  try:
    #Config.read("config.ini")
    return Config.getint(section, name)
  except:
    return 0
    
def getBool(section, name):
  try:
    Config.read("config.ini")
    return Config.getboolean(section, name)
  except:
    return 0
    
    