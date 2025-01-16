
import re
from datetime import datetime
import math

def StringCheck(value,lenght,specialchar = None):
    if(len(value)>lenght):
        return False
    if(not re.findall(r"^[A-Za-z0-9]*$",value)):
        return False
    if(specialchar and re.findall(f"{specialchar}",value)):
        return False
    return True

def NumberCheck(value,lenght = math.inf,specialchar = None,negative = True):
    if(len(value)>lenght):
        return False
    if(not re.findall(r"^[-0-9]*$",value)):
        return False
    if specialchar and re.search(re.escape(specialchar), value):
        return False
    if(negative == False and float(value) <0):
        return False
    return True

def DateCheck(value,specialchar = "-"):
    date_format="%Y-%m-%d"
    date_format = date_format.replace("-", specialchar)
    try:
        datetime.strptime(value, date_format)
    except ValueError:
        return False
    else:
        return True
    
def BoolCheck(value,true,false):
    if value == true or value == false:
        return True
    else:
        return False

def EnumCheck(value,enum):
    if(value in enum):
        return True
    else:
        return False
    
def TimeCheck(value):
    try:
        datetime.strptime(value, "%H:%M:%S")
    except ValueError:
        return False
    else:
        return True