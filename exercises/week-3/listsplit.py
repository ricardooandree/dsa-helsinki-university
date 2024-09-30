""" Description:
You are given a list containing n integers. Your task is to count, how many ways you can split the list into two parts so that both parts have the same smallest element.
The time complexity of the algorithm should be O(n).
In a file listsplit.py, implement a function count that returns the desired count.
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0