from boyer import clear
from tools import generate
password = generate(readability=True, max_length=20, difficulty=True)
print(password)
