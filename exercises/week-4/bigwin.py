""" Description:
You are given the price of a stock for n days. Your friend tells you the they bought the stock on one day and sold the stock at a double the price on another day. How many ways this could have happened?
The time complexity of the algorithm should be O(n).
In a file bigwin.py, implement a function count that returns the number of ways.
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([1,2,3,4])) # 2
    print(count([1,1,1,1])) # 0
    print(count([1,2,1,2,1,2])) # 6
    print(count([5,1,3,4,1,6])) # 1