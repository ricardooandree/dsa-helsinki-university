""" Description:
Extend the class TreeSet given in the lecture material by adding a method __len__ that returns the number of elements in the set.

In a file treesize.py, implement the class TreeSet according to the following template.
"""


class TreeSet:
    # methods in the course material

    def __len__(self):
        # TODO
        pass

if __name__ == "__main__":
    s = TreeSet()
    print(len(s)) # 0
    s.add(1)
    print(len(s)) # 1
    s.add(2)
    print(len(s)) # 2
    s.add(3)
    print(len(s)) # 3
    s.add(2)
    print(len(s)) # 3