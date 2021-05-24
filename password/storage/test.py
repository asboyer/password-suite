import json

with open("passwords.json", "r") as file:
    passwords = json.load(file)

print(passwords)