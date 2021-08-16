#Dictionary
print(dir({}))

# empty dictionary
print(my_dict = {})

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
y_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

#Accessing Elements from Dictionary
# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])

#Changing and Adding Dictionary elements
# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

#Removing elements from Dictionary
# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)

#https://www.programiz.com/python-programming/dictionary


#Dictionary (Other languages : map, objects , hash)
statesAndCapitals = {
                     'Gujarat' : 'Gandhinagar',
                     'Maharashtra' : 'Mumbai',
                     'Rajasthan' : 'Jaipur',
                     'Bihar' : 'Patna'
                    }

print(statesAndCapitals)
#To get both keys and their values
for _ in statesAndCapitals.items():
    print(_)

#To get keys of the dictionaries
for keys in statesAndCapitals.keys():
    print(keys)
#To get values of the dictionaries
for values in statesAndCapitals.values():
    print(values)

#dictionary comprehension
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)







user = dict({"user": ['vignesh','sajal'],
            "designation": ['data scientist','data scientist']})

print(type(user))


user ={

    "basket" : [1,2,3,4],
    "greet"  : "hellloo"
}

#print(user['age'])
#When the given key is not in dictionary we can use get method just to avoid errors.
print(user.get('age', 27))


