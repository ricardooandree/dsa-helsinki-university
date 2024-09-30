""" Description:
You are given a list containing n integers. Your task is to pick as many integers from the list as possible. The first number picked can be any number on the list. Each of the other numbers must be exactly one larger than the preceding number. How many numbers can you pick?
The time complexity of the algorithm should be O(n \log n).
In a file interval.py, implement the function count that returns the maximum number of integers that can be picked as described.
"""


""" Explanation:
Explanation: From the list [10, 4, 8] we can pick only one number, since no two numbers differ by exactly 1. From the list [7, 6, 1, 8] we can pick 3 numbers in the order 6, 7 and 8.
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3