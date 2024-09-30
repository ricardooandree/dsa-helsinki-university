""" Description: You are given the price of a stock for n days. Your task is to figure out the highest profit you could have made, if you could have bought and sold the stock at most twice.
At any time, you may hold at most one share of the stock. If you buy again after selling, there must be at least one day of no shares held in between the sale and the following buy.
The time complexity of the algorithm should be O(n).
In a file trading.py, implement a function `find' that returns the desired result.
"""

""" Explanation:
Explanation: When the prices are [1,5,2,1,5], the profit 8 is earned by twice buying at the price 1 and selling at the price 5. When the prices are [1,5,1,5], this is no more possible because there must be one day between the first sell and the second buy. Thus you can get the profit 4 only once.
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10