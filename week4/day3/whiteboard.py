# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:						
# Input: ‘Joel’
# Output: ‘Jl’
# Input: ‘Shoha’
# Output: ‘Shh’

import re

string = "Joel"

def whiteboard(string):
    print(re.sub("[AEIOUaeiou]", "", string))

whiteboard(string)

# string = "Shoha"

# def whiteboard2(string):
#     return "".join(x for x in string if x.lower() not in {"a","e",'i','o','u'})

# print(whiteboard2(string))