""" Description:
You are given a list of n integers. Your task is to find a longest increasing subsequence of the list. If there are multiple solutions, you may return any of them.
You may assume that 1 <= n <= 100. The algorithm should be efficient in all these cases.
In a file createseq.py, implement a function find that returns the desired answer.
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]