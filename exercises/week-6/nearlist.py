""" Description:
Your task is to implement the class NearList that is given a list of numbers in the constructor.
The class should have an efficient method find(x) that finds the list number that is nearest to the number x by value. If the answer is not unique, the method should return the smaller number.
You may assume that all the numbers in the task are integers.
In a file nearlist.py, implement a class NearList according to the following template:
"""


class NearList:
    def __init__(self, t):
        # TODO
        pass

    def find(self, x):
        # TODO
        pass

if __name__ == "__main__":
    n = NearList([3, 6, 1, 3, 9, 8])
    print(n.find(1)) # 1
    print(n.find(2)) # 1
    print(n.find(3)) # 3
    print(n.find(4)) # 3
    print(n.find(5)) # 6
    print(n.find(6)) # 6
    print(n.find(7)) # 6
    print(n.find(8)) # 8
    print(n.find(9)) # 9