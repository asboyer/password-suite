from random import randint
from random_word import RandomWords


# words
words = RandomWords()

# alphabet characters
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()

# numbers
nums = '0123456789'

# specials
special = '!@#$%&_'

# all chars
all_chars = lower + upper + nums + special

def choice(string):
    i = randint(0, len(string) - 1)
    return string[i]

def generate(min_length=12, max_length=14, readability=False):
    length = randint(min_length, max_length)
    
    if readability:
        # nums -
        # special - 
        # lowercase
        # uppercase

        password = []

        numSpecials = randint(1, length/(length/2))
        numNums = randint(1, length/(length/2))

        remainingLength = length - numSpecials - numNums

        specialsIn = ''
        numsIn = ''

        for i in range(numNums):
            numsIn += choice(nums)
        for i in range(numSpecials):
            specialsIn += choice(special)

        firstNum = randint(2, remainingLength - 3)
        secondNum = remainingLength - firstNum

        firstWord = None
        secondWord = None

        while firstWord == None or secondWord == None:
            firstWord = words.get_random_word(hasDictionaryDef="true", minLength=firstNum, maxLength=firstNum)
            secondWord = words.get_random_word(hasDictionaryDef="true", minLength=secondNum, maxLength=secondNum)


        print(firstWord, firstNum, len(firstWord))
        print(secondWord, secondNum, len(secondWord))

        newFirst = ''
        newSecond = ''

        for char in firstWord:
            cap = randint(0, 1)
            if cap == 0:
                newFirst += char
            else:
                newFirst += char.upper()

        for char in secondWord:
            cap = randint(0, 1)
            if cap == 0:
                newSecond += char
            else:
                newSecond += char.upper()

        password = [numsIn, specialsIn, newFirst, newSecond]

        print(password)


    if not readability:
        password = ''

        for i in range(length):
            password += choice(all_chars)
        
        return password