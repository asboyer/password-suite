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

def shuffle(l):
    l2 = []
    while len(l) > 0:
        c = choice(l)
        l2.append(c)
        l.remove(c)
    return l2

def memify(text):
    new = []
    for i in text:
        r = randint(0, 1)
        if r == 1:
            new.append(i.upper())
        else:
            new.append(i.lower())
    new = ''.join(new)
    return new

def generate(min_length=12, max_length=14, readability=False):
    
    # goal - generate a password with words, mixed in with a few special chars + nums

    length = randint(min_length, max_length)

    if readability:
        # nums -
        # special - 
        # lowercase
        # uppercase

        password = []
        numSpecials = randint(1, int(length / 10) * 2) 
        numNums = randint(1, int(length / 10) * 2)

        remainingLength = length - numSpecials - numNums

        specialsIn = ''
        numsIn = '' #

        for i in range(numNums):
            numsIn += choice(nums) #
        for i in range(numSpecials):
            specialsIn += choice(special)

        firstLen = randint(2, remainingLength - 3)
        secondLen = remainingLength - firstLen

        firstWord = None
        secondWord = None

        while firstWord == None or secondWord == None:
            firstWord = words.get_random_word(hasDictionaryDef="true", minLength=firstLen, maxLength=firstLen)
            secondWord = words.get_random_word(hasDictionaryDef="true", minLength=secondLen, maxLength=secondLen)

        newFirst = ''
        newSecond = ''


        # make a memify
        # for char in firstWord:
        #     cap = randint(0, 1)
        #     if cap == 0:
        #         newFirst += char
        #     else:
        #         newFirst += char.upper()

        # for char in secondWord:
        #     cap = randint(0, 1)
        #     if cap == 0:
        #         secondFi += char
        #     else:
        #         newFirst += char.upper()

        for char in numsIn + specialsIn: # 
            password.append(char)

        password.append(firstWord)
        password.append(secondWord)

        password = shuffle(password)

        finalPass = ''
        for st in password:
            finalPass += st

        return finalPass.replace(' ', '').replace('.', '_')   



    if not readability:
        password = ''

        for i in range(length):
            password += choice(all_chars)
        
        return password