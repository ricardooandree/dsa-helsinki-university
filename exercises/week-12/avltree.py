""" Description:
Implement the class TreeSet based on the AVL tree as described in the course material.

In a file avltree.py, implement the class TreeSet according to the following template.
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

if __name__ == "__main__":
    s = TreeSet()
    s.add(1)
    s.add(2)
    s.add(4)
    print(1 in s) # True
    print(2 in s) # True
    print(3 in s) # False
    print(4 in s) # True
    print(s) # [1, 2, 4]