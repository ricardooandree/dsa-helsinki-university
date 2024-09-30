""" Description:
Extend the class TreeSet by adding the methods prev and next that return the predecessor and the successor elements as described in the course material.
If there is no such element, return None.

In a file prevnext.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    # methods in the course material

    def prev(self, x):
        # TODO
        pass

    def next(self, x):
        # TODO
        pass
    
if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5)) # 2
    print(s.prev(2)) # None
    print(s.next(1)) # 2
    print(s.next(2)) # 5
    print(s.next(5)) # None