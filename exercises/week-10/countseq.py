""" Description:
You are given a list of n integers. Your task is to count how many increasing subsequences does the list contain.
You may assume that 1 <= n <= 100. The algorithm should be efficient in all these cases.
In a file countseq.py, implement a function count that returns the desired answer.
"""

""" Explanation:
Explanation: The list [1,1,2,2,3,3] contains the increasing subsequences [1,2,3] (8 times), [1,2] (4 times), [1,3] (4 times), [2,3] (4 times), [1] (2 times), [2] (2 times) and [3] (2 times).
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37