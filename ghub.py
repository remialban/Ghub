#!/usr/bin/env python
import sys
#sys.path.append('/home/remi/Documents/ghub')
from functions import *
try:
    command = sys.argv[1]
except:
    help()
    exit()

value = None
try:
    value = sys.argv[2:]
except:
    pass

switcher = {
        "new": new,
        "remove": remove,
        "push": push,
        "update": update,
        "run": run,
        "init": init,
    }

switcher.get(command, help)(command, value)