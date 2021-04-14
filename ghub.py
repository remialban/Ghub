#!/usr/bin/env python
import sys
sys.path.append('/home/remi/Documents/ghub')
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
    "help": help
}

try {
    switcher.get(command, help)(command, value)
} except {
    print("This command is incorrect")
    help(command, value)
}
