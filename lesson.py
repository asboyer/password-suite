# dictionaries

# lists
l = [1, 2, 3, 4]

arr2D = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#         0  1  2
#            0          1            2

# tuples
tupl = (1, 2, 3)

#tupl[0]  tupl[1]  tupl[2]
(alek,    two,     three) = tupl

# sets

myset = {"apple", "banana", "cherry", "apple", "papaya"}

myset.add("orange")

alekset = {"pineapple", "mango", "watermelon", "dragonfruit", "papaya", "apple"}

# myset.update(alekset)
# ^             ^
# |             |______________ stays the same  
# the on that gets update (updates the set with the values from set in ())

# newset = myset.union(alekset)

# alekset.intersection_update(myset)

# anotherset = alekset.intersection(myset)

# alekset.symmetric_difference_update(myset)

lastset = symmetric_difference(myset)

print(alekset)