""" Description:
You are given a list containing n integers. Your task is to find the longest distance between two occurrences of the same number. A distance means the difference of the indices.
The time complexity of the algorithm should be O(n).
In a file samedist.py implement a function find that returns the longest distance.
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4