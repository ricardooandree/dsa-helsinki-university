""" Description:
You are given n coin values and a sum x. Find the maximum number of coins that sum up to x.
You may assume that 1 <= n <= 10 and that 1 <= x <= 100. One of the coin values is always 1. The algorithm should be efficient for all these cases.
In a file maxcoin.py, implement a function find that returns the desired count.
"""

""" Explanation:
Explanation: When x=5 and the coins are [1,2,5], the optimal solution is [1,1,1,1,1], which contains 5 coins.
"""


def find(x, coins):
    # TODO
    pass

if __name__ == "__main__":
    print(find(5, [1, 2, 5])) # 5
    print(find(10, [1])) # 10
    print(find(8, [1, 2, 3, 4, 5])) # 8