""" Description:
You are given n coin values and a sum x. How many ways can you choose the coins so that they sum up to x and so that the number of coins is the smallest possible?
You may assume that 1 <= n <= 10 and that 1 <= x <= 100. One of the coin values is always 1. The algorithm should be efficient in all these cases.
In a file minways.py, implement a function count that returns the desired count.
"""

""" Explanation:
Explanation: When x=5 and the coin values are [1,2,3,4], there are 4 different ways: [1,4], [2,3], [3,2] and [4,1].
"""


def count(x, coins):
    # TODO
    pass

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30