#Remember that an object is something a variable can refer to.
#The is operator will return true if the two references are to the same object.

"""
a = "banana"
b = "banana"

print(a is b) #this is a string 
"""


a = [81, 82, 83]
b = [81, 82, 83]

print(a is b) #why is this false 

print(a == b) #why is this true 
#well bc these are lists and a and b have the same value but do not refer to the same object.


