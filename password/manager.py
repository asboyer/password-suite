import json, os

from boyer import clear

class terminate(Exception): pass

if os.path.exists("storage/passwords.json"):
    with open("storage/passwords.json", "r") as file:
        passwords = json.load(file)
else:
    passwords = {}

def user_cmd(cmd):
    cmd_raw = cmd
    cmd = cmd.lower().strip()
    if cmd == 'quit':
        quit()
    elif cmd.startswith('man') or cmd.startswith('help') or cmd.startswith('how'):
        man()
    elif cmd == 'cls' or cmd == 'clear':
        clear()
    elif cmd == 'new':
        new()
    else:
        print('Not a command!')

def save():
    with open("storage/passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def quit():
    # save new files and credentials added in this session
    save()
    raise terminate

def man():
    pass

def new():
    name = input("Password name: ")
    passwords[name] = {}
    
    username = input(f"Username for {name}: ")
    passwords[name]["username"] = username

    password = input(f"Password for {name}: ")
    passwords[name]["password"] = password

    save()

while True:
    try:
        cmd = input("User command: ")
        user_cmd(cmd)
    except terminate:
        break




