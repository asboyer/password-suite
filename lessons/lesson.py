# # lists
# l = [1, 2, 3, 4]

# arr2D = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# #         0  1  2
# #            0          1            2

# # tuples
# tupl = (1, 2, 3)

# #tupl[0]  tupl[1]  tupl[2]
# (alek,    two,     three) = tupl

# # sets

# myset = {"apple", "banana", "cherry", "apple", "papaya"}

# myset.add("orange")

# alekset = {"pineapple", "mango", "watermelon", "dragonfruit", "papaya", "apple"}

# # myset.update(alekset)
# # ^             ^
# # |             |______________ stays the same  
# # the on that gets update (updates the set with the values from set in ())

# # newset = myset.union(alekset)

# # alekset.intersection_update(myset)

# # anotherset = alekset.intersection(myset)

# # alekset.symmetric_difference_update(myset)

# lastset = symmetric_difference(myset)

# print(alekset)


# dictionaries

dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "electric": False,
  "colors": ["red", "white", "blue"],
  "owners": {

        "Kent": {
            
            "address": "41 Bridge Road",
            
            "siblings": {
                
                "Amy": {
                    "address": "411 Bridge Road",
                },
            
            "car_price": 1900
            
            }
        },

        "Alek": {
            "address": "42 Bridge Road"
        },

        "Andrew": {
            "address": "Beverly Drive Road"
        }
  }
}

# print(dictionary["brand"])
# print(dictionary["year"])
# print(dictionary["model"])
# keys and values

# print(dictionary["owners"]["Andrew"].get("address"))
# print('\n___________\n')
# print(dictionary.get("owners").get("Andrew").get("address"))

x = dictionary.keys()

# for i in x:
#     print(i)


stars = {
    "Darth Vader": {
        "lightsaber-color": "red",
        "side": "sith",
        "movies": [1, 2, 3, 4, 5, 6]
    },
    "Darth Vader": {
        "lightsaber-color": "red",
        "side": "sith",
        "movies": [1, 2, 3, 4, 5, 6]
    },
    "Darth Vader": {
        "lightsaber-color": "red",
        "side": "sith",
        "movies": [1, 2, 3, 4, 5, 6]
    }
}

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}




x = car.items()

x = car.values()

car["new"] = True

car.update({"year": 2020})

print(car)

car.pop("new")

del car["year"]

# print(car)

# car.clear()

print(car)

for x, y in car.items():
    print(x, y)

car1 = car # car1 will only be a reference to car, changes made in car1 will affect car
