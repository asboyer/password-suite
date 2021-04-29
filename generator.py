from boyer import clear
from tools import generate

clear()

print('Readability:')
for i in range(5):	
	print(generate(readability=True))

print('\nNormal:')
for i in range(5):	
	print(generate(readability=False))
print('\n')
