# Ghub

This application allows you to make your life easier on ```git``` cli.
To use this application you must downlaod ```git``` cli and this repository.
To use ```ghub``` cli you must write on your terminal.
```
python /path/to/your/ghub/repository/ghub.py <command> [args]
```

## Commands:

- Clone repository from git server (for exemple Github)
```
python ghub.py new <project name> <url of respository>
```
```<project name>``` is optionnal
- Commit and send the modification to server
```
python ghub.py push <commit name>
```
The commit name argument is not mandatory
- Remove ghub project (locally)
```
python ghub.py remove /path/of/project/directory
```
- Update a project : update from git server to your computer
```
pyhon ghub.py update
```

## Ghub.json
When you create a ghub project, ghub create a ```ghub.json``` file :
```
{
  "name": "my-project",
  "commands": {
    "test": "echo Hello World !"
  }
}
```
If there is not the ```ghub.json``` file you aren't in ghub project. To init ghub project you must run this command :
```
python ghub.py init
```
On your ```ghub.json```, there is the name of your ghub project. On this file, there is the commands list. By default, there is a ```test``` command. Run on your terminal this command :
```
python ghub.py run test
```
You can see a ```Hello world !``` message. You can create your own command (or many commands). For this exemple, I will add a ```start``` command who run ```python main.py``` command :
```
{
  "name": "my-project",
  "commands": {
    "test": "echo Hello World !",
    "start": "python main.py"
  }
}
```
To run this command you have just to run :
```
python ghub.py run start
```
The command name must be just one word.
If the name of the command is ```run```, you can just run this command : 
```
python ghub.py run
```
or you can always run this command :
```
python ghub.py run run
```
```
{
  "name": "my-project",
  "commands": {
    "test": "echo Hello World !",
    "run": "python main.py"
  }
}
```
