""" Description:
Initially the list contains the integer 1. In each step, you delete the smallest element x from the list and then add the elements 2x and 3x into the list. What is the smallest element of the list after n steps?
For example when n=5, the list changes as follows:
[1] -> [2,3] -> [3,4,6] -> [4,6,6,9] -> [6,6,9,8,12] -> [6,9,8,12,12,18]

In this case, the smallest element at the end is 6.
The time complexity of the algorithm should be O(nlog n).
In a file twothree.py, implement a function smallest that returns the desired answer.
"""


def smallest(n):
    # TODO
    pass

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552