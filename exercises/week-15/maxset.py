""" Description:
Initially each of the numbers 1,2,...,n is in its own set. Your task is to implement a class that supports merging two sets and finding the size of the largest set.
Implement a class MaxSet with the following methods:

merge merges the sets containing the numbers a and b (if they are in different sets)
get_max reports the size of the largest set

Implement the class in a file maxset.py according to the following template:
"""


class MaxSet:
    def __init__(self, n):
        # TODO
        pass

    def merge(self, a, b):
        # TODO
        pass

    def get_max(self):
        # TODO
        pass

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max()) # 3
    m.merge(1, 5)
    print(m.get_max()) # 5