""" Description:
A grid has n*n squares, which are all walls initially. The rows and columns are numbered 1 ... n. The walls are then gradually removed by converting them into floor squares.
Your task is to keep track of the number of rooms during the process. A room consists of vertically or horizontally connected floor squares, as in earlier problems on the course.
Implement a class WallGrid with the following methods:

remove converts the square (x,y) into a floor if it is not already a floor
count returns the number of rooms

The methods should be efficient even on large grids.
Implement the class in a file wallgrid.py according to the following template:
"""


class WallGrid:
    def __init__(self, n):
        # TODO
        pass

    def remove(self, x, y):
        # TODO
        pass

    def count(self):
        # TODO
        pass

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2, 2)
    w.remove(4, 2)
    print(w.count()) # 2
    w.remove(3, 2)
    print(w.count()) # 1
    w.remove(2, 4)
    w.remove(2, 4)
    w.remove(4, 4)
    print(w.count()) # 3
    w.remove(3, 3)
    print(w.count()) # 3
    w.remove(3, 4)
    print(w.count()) # 1