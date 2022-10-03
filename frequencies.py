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



# Function 2
def frequencies2(items):

    # using Counter to find frequency of elements
    frequencies = collections.Counter(items)

    # return the frequencies
    return (dict(frequencies))



