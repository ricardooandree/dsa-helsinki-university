""" Description:
Construct a list that contains the numbers 1 ... n so that no two consecutive numbers are adjacent on the list.
If there are multiple solutions, the first element should be as small as possible. If there are still multiple solutions, the second element should as small as possible, and so on. In other words, the list should be lexicographically as small as possible.
You may assume that 1 <= n <= 100. The algorithm should be efficient in all these cases.
In a file morediff.py, implement a function create that returns the list. If there is no solution, the function should return None.
"""


def create(n):
    # TODO
    pass

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]