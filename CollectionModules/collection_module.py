import collections
from collections import ChainMap, Collection, Counter, namedtuple
from typing import Deque, NamedTuple

# Counter
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))


# NamedTuple
def cus_rem(x,y):
    DivMod = namedtuple("Divmod", "quotient_remainder")
    return DivMod(divmod(x,y))

result = cus_rem(10,5)
print(result)

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
   
# Adding values
S = Student('Nandini','19','2541997')

# initializing iterable 
li = ['Manjeet', '19', '411997' ]
   
# initializing dict
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
   
# using _make() to return namedtuple()
print ("The namedtuple instance using iterable is  : ")
print (Student._make(li))
   
# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is  : ")
print (S._asdict())


# Deque
from collections import deque
# Declaring deque
queue = deque(['name','age','DOB'])   
print(queue)

# inserts 4 at the end of deque
queue.append(4)
queue.appendleft(6)
queue.pop()
queue.popleft()
print(queue)

from collections import UserDict, UserList, UserString

# Creating a Mutable String
class Mystring(UserString):
       
    # Function to append to
    # string
    def append(self, s):
        self.data += s
           
    # Function to remove from 
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")
       
# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)
   
# Appending to string
s1.append("s")
print("String After Appending:", s1.data)
   
# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)

class MyList(UserList):
       
    # Function to stop deletion
    # from List
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")
           
    # Function to stop pop from 
    # List
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
       
# Driver's code
L = MyList([1, 2, 3, 4])
   
print("Original List")
   
# Inserting to List"
L.append(5)
print("After Insertion")
print(L)
   
# Deleting From List
L.remove()

class MyDict(UserDict):
       
    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
           
    # Function to stop pop from 
    # dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
           
    # Function to stop popitem 
    # from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")
       
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})
   
d.pop(1)

# OrderedDict
from collections import OrderedDict   
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
   
for key, value in d.items():
    print(key, value)
   
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
   
for key, value in od.items():
    print(key, value)


# defaultdict
from collections import defaultdict  
# Defining a dict
d = defaultdict(list)
   
for i in range(5):
    d[i].append(i)
       
print("Dictionary with values as list:")
print(d)

# ChainMap

from collections import ChainMap    
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
 
# Defining the chainmap
c = ChainMap(d1, d2, d3)
    
print(c)












