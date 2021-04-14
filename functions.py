import os
import shutil
import json

def is_ghub_project(path=""):
    if(os.path.exists(path + "ghub.json")):
        return True
    return False

def create_json_file(name="my-project", path=""):
    
    if(os.path.exists(path + "ghub.json")):
        print("You have already a ghub.json file")
        exit()
    fichier = open(path + "ghub.json", "x")
    ghub = {
        "name": name,
        "commands": {
            "test": "echo Hello world !"
        }
    }

    fichier.write(json.dumps(ghub,indent = 4))
    fichier.close()

def help(command, value):
    print("Error")

def new(command, value):
    if(len(value) == 2):
        url = value[1]
        name = value[0]
    elif(len(value) == 1):
        url = value[0]
        name = "my-project"
    else:
        print("Error")
        exit()
    os.system("git clone " + url + " " + name)
    create_json_file(name, name + "/")

def remove(command, value):
    if(is_ghub_project(value[0] + "/")):
        shutil.rmtree(value[0])
    else:
        print("This directory does not exist or this directory is not a ghub project.\nTo init a ghub project you muse use this command : ghub init")

def push(command, value):
    message = "Add file via upload"
    if(len(value) == 1):
        message = value[0]
    print(message)
    if(is_ghub_project()):
        os.system("git add -A")
        os.system("git commit -m \"" + message + "\"")
        os.system("git push")

def update(command, value):
    if(is_ghub_project()):
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
        command_name = value[0]
    except:
        command_name = "run"
    try:
        command = commands.get(command_name)
    except:
        print("The \""+value[0]+"\" doesn't exist. You can add a \"" + value[0] + "\" command in your ghub.json file.")
        exit()
    
    os.system(command)

def init(command, value):
    create_json_file(os.path.basename(os.getcwd()))