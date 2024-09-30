""" Description:
Extend the class TreeSet by adding the methods min and max that return the smallest and the largest element in the set as described in the course material.
If the set is empty, return None.

In a file minmax.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    # methods in the course material

    def min(self):
        # TODO
        pass

    def max(self):
        # TODO
        pass
    
if __name__ == "__main__":
    s = TreeSet()
    print(s.min()) # None
    print(s.max()) # None
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.min()) # 1
    print(s.max()) # 3