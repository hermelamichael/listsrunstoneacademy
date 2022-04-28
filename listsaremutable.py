#Unlike strings, lists are mutable. This means we can change an item in a list by 
# accessing it directly as part of the assignment statement.

'''
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit) #cant do this sauce with strings 
''' 

"""
#arrow down
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)
"""

'''
alist = ['a', 'd', 'f']
print(alist[1:1]) #= ['b', 'c'] #empty string which makes sense 
#print(alist)
#alist[4:4] = ['e']
#print(alist)
'''

'''
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist) #squeezes and adds does not replace adds before 
alist[4:4] = ['e']
print(alist)
'''

