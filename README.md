# Ghub

This application allows you to make your life easier on ```git``` cli.
To use this application you must downlaod ```git``` cli and this repository.
To use ghub cli you must write on your terminel
```
python /path/to/your/ghost/repository/ghost.py command [args]"
```

## Commands:

- Clone repository from git server (for exemple Github)
```
python ghost.py new <url of respository>
```
- Commit and send the modification to server
```
python ghost.py push <commit name>
```
The commit name argument is not mandatory
- Remove ghost project (locally)
```
python ghost.py remove /path/of/project/directory
```
- Update a project : update from git server to your computer
```
pyhon ghost.py update
```
