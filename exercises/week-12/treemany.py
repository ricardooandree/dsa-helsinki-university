""" Description:
Modify the class TreeSet so that the same element can occur multiple times in the set.
This requires changes in the methods given in the course material. 
In addition, implement a method count that reports how many times the given element occurs in the set.

In a file treemany.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    def add(self, x):
        # TODO
        pass

    def __contains__(self, x):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass

    def count(self, x):
        # TODO
        pass

if __name__ == "__main__":
    s = TreeSet()
    s.add(4)
    s.add(1)
    s.add(2)
    s.add(1)
    print(s) # [1, 1, 2, 4]
    print(1 in s) # True
    print(2 in s) # True
    print(3 in s) # False
    print(4 in s) # True
    print(s.count(1)) # 2
    print(s.count(2)) # 1
    print(s.count(3)) # 0
    print(s.count(4)) # 1