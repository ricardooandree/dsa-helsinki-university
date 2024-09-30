""" Description:
Your task is to count how many balanced parenthesis sequences of length n have at most k nested pairs of parenthesis.
You may assume that 2 <= n <= 16 and that 1 <= k <= n/2. The algorithm should be efficient in all these cases.
In a file brackets.py, implement a function count that returns the desired count.
"""


def count(n, k):
    # TODO
    pass

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094