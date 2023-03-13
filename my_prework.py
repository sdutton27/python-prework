# Name: Simon Dutton
# Date: due March 13, 2023 11:59PM
# My Prework for Padawans-115
# Coding Temple PT Course

# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. 
def hello_name(user_name):
    """Prints 'hello_USERNAME!' The USERNAME is the input, capitalized."""
    print(f"hello_{user_name.upper()}!")

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing
def first_odds():
    """Prints the odd numbers from 1-100."""
    num = 1 # init variable
    while num <= 100:
        if num % 2 == 1: #odd
            print(num)
        num += 1

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of 
# a given list. 
def max_num_in_list(a_list):
    """Returns the maximum number in a given list of numbers."""
    return sorted(a_list)[-1] #note: this assumes the list is made of numbers

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Returns if the given year is a leap year."""
    return(a_year % 4 == 0 and (not a_year % 100 == 0 or 
                                (a_year % 100 == 0 and a_year % 400 == 0)))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
# are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """Checks if all numbers in a given list are consecutive numbers."""
    counter = a_list[0] # init counter
    for num in a_list:
        if counter != num: # next number is not consecutive
            return False
        counter += 1    
    return True