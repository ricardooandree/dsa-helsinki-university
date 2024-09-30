""" Description:
Binary search is an efficient algorithm for searching an element in a sorted list. The idea is to start the search in the middle of the list, so that the search area that might contain the element can be immediately reduced to half.
Search the internet for information about binary search and study how it works.
Implementing binary search correctly is surprisingly difficult. For example, the implementation below is incorrect:
"""


def binary_search(items, x):
    left = 0
    right = len(items) - 1

    while left < right:
        middle = (left + right) // 2

        if items[middle] == x:
            return True

        if items[middle] > x:
            right = middle - 1
        else:
            left = middle + 1

    return False

numbers = [1, 3, 8]

print(binary_search(numbers, 2)) # False
print(binary_search(numbers, 3)) # True
print(binary_search(numbers, 4)) # False


""" Description:
Study the above function, and find three examples of inputs that cause the function to produce an incorrect output.
In this task, you get a point automatically when you fill in your results and press the submit button.
"""


# TODO What inputs did you find and how did you find them?