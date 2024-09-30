""" Description:
Extend the class TreeSet by adding the method remove that removes the given element from the set as described in the course material.
If the element is not in the set, do nothing.

In a file treerem.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    # methods in the course material

    def remove(self, x):
        # TODO
        pass
    
if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(1)
    s.add(3)
    s.add(4)
    print(s) # [1, 2, 3, 4]
    s.remove(3)
    print(s) # [1, 2, 4]
    s.remove(2)
    print(s) # [1, 4]
    s.remove(1)
    print(s) # [4]
    s.remove(1)
    print(s) # [4]