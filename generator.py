from boyer import clear
from tools import generate
<<<<<<< HEAD
password = generate(readability=True, max_length=20)
print(password)
=======

clear()

print('Readability:')
for i in range(5):	
	print(generate(readability=True))

print('\nNormal:')
for i in range(5):	
	print(generate(readability=False))
print('\n')
>>>>>>> 4c14b05734e389046800fa689cf834c90392b701
