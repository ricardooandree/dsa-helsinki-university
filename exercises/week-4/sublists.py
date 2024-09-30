""" Description:
You are given a list containing n integers. Your task is to count how many sublists have the sum 0 and additionally have the same first and last number.
The time complexity of the algorithm should be O(n).
In a file sublists.py, implement a function count that returns the number of sublists.
"""


""" Explanation:
Explanation: In the last test, the sublists are [1,-2,1], [1,-2,1,-1,1] and [1,-2,1,-1,1,-1,1].
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([2,3,-7,2])) # 1
    print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3