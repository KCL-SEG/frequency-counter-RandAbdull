"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


# importing the module
import collections



# Function 1
def frequencies(items):
    frequencies = {}

    # iterating over the list
    for item in items:
       # converting item to string
       item = str(item)
       # checking the element in dictionary
       if item in frequencies:
          # incrementing the counr
          frequencies[item] += 1
       else:
          # initializing the count
          frequencies[item] = 1
    
    return frequencies





