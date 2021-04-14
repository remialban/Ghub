import os
import shutil
import json

def help(command, value):
    print("erreur")

def new(command, value):
    os.system("git clone " + value[0])

def remove(command, value):
    if(os.path.exists(value[0] + "/.git")):
        shutil.rmtree(value[0])
    else:
        print("This directory does not exist or this directory is not a git project")

def push(command, value):
    message = "Add"
    if(len(value) == 1):
        message = value[0]
    print(message)
    if(os.path.exists(".git")):
        os.system("git add -A")
        os.system("git commit -m \"" + message + "\"")
        os.system("git push")

def update(command, value):
    if(os.path.exists(".git")):
        os.system("git pull")

def run(command, value):
    file = open("ghub.json")
    json_result = file.read()
    tab = json.loads(json_result)
    try:
        commands = tab.get("commands")
    except:
        print("You haven't commands in your ghub.json")
        exit()
    
    try:
        command = commands.get(value[0])
    except:
        print("The \""+value[0]+"\" doesn't exist. You can add a \"" + value[0] + "\" command in your ghub.json file.")
    os.system(tab.get("commands").get(value[0]))

def init(command, value):
    if(os.path.exists("ghub.json")):
        print("You have already a ghub.json file")
        exit()
    fichier = open("ghub.json", "x")
    
    ghub = {
    "name": os.path.basename(os.getcwd()),
    "commands": {
        "test": "echo Hello world !"
    }

}
    fichier.write(json.dumps(ghub,indent = 4))
    fichier.close()

print(os.getenv("HOME"))