""" Description:
You are given a list consisting of n integers. n-1 of the integers are equal and one has a different value. Your task is to determine what the different integer is.
The time complexity of the algorithm should be O(n). You may assume that n>2.
In a file onlyone.py, implement a function find that returns the desired integer.
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5