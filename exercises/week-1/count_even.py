""" Description:
The course material includes two different ways to implement the function count_even:

Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
In this exercise, you get a point automatically when you submit the test results and the code that you used.
"""

# Implementation 1
def count_even_one(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# Implementation 2
def count_even_two(numbers):
    return sum(x % 2 == 0 for x in numbers)


# TODO Implementation 1 run time: s
# TODO Implementation 2 run time: s
