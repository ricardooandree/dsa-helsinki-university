""" Description:
Extend the class TreeSet given in the lecture material by adding a method height that returns the height of the binary search tree.

In a file treeheight.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    # methods in the course material

    def height(self):
        # TODO
        pass
    
if __name__ == "__main__":
    s = TreeSet()
    print(s.height()) # -1
    s.add(2)
    print(s.height()) # 0
    s.add(1)
    print(s.height()) # 1
    s.add(3)
    print(s.height()) # 1
    s.add(4)
    print(s.height()) # 2