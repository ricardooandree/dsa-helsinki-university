""" Description: 
You are given a list containing n integers. Every number has exactly two occurrences on the list, except one number that occurs only once. Your task is to find this number.
The time complexity of the algorithm should be O(n).
In a file nopair.py, implement a function find that returns the desired number.
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([2,1,3,2,3])) # 1
    print(find([5,5,9])) # 9
    print(find([1,2,3,4,1,3,4])) # 2
    print(find([8])) # 8
    print(find([7,1,7,4,4,5,1])) # 5