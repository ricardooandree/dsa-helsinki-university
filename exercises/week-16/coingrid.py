""" Description:
You are given an n*n grid where some squares contain a coin. In the grid description, the character . stands for an empty square and the character X stands for a coin.
In one step, you can collect all the coins from a row or a column of your choice. What is the smallest number of steps needed to collect all the coins?
In a file coingrid.py, implement a function count that returns the smallest number of steps needed to collect all coins.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r =["........",
        "........",
        "...X..X.",
        "........",
        "....X...",
        "..X.X..X",
        "........",
        "....X..."]
    print(count(r)) # 3