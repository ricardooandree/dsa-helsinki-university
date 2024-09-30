""" Description:
Your task is to create a list containing the numbers 1 ... n so that the number of inversions is exactly k.
You may assume that n <= 100 and that k is chosen so that a solution exists. Any valid solution is acceptable.
In a file againinv.py, implement a function create that returns the desired list.
"""


def create(n, k):
    # TODO
    pass

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]