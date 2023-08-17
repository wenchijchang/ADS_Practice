# Task 1: Even or Odd
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.










# Task 2: Less than 100
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.










# Task 3: Repeated Names
# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.










# Task 4: Sort List
# Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.

def sort_list(arr):

    # build algorithm here

    return arr

unsorted = [6, 8, 3, 4, 7, 2]
sorted = sort_list(unsorted)
# sorted should be [2, 3, 4, 6, 7, 8]
