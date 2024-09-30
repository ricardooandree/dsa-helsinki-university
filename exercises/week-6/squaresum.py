""" Description:
When the data contains the observations (x_1,y_1),(x_2,y_2),...,(x_n,y_n) and the line y=ax+b is fitted to the data, the error can be computed with the sum of squares formula

Sum(yi - (axi + b))^2

For example, when the data is (1,1),(3,2),(5,3) and the line is y=x-1 (i.e., a=1 and b=-1), the error is (1-(1-1))^2+(2-(3-1))^2+(3-(5-1))^2=2.

Implement a class SquareSum with the methods

add(x, y): add an observation to the data
calc(a, b): return the sum of squares error for the given line parameters

The time complexity of both methods should be O(1).
In a file squaresum.py, implement a class SquareSum according to the following template:
"""


class SquareSum:
    def __init__(self):
        # TODO
        pass

    def add(self, x, y):
        # TODO
        pass

    def calc(self, a, b):
        # TODO
        pass

if __name__ == "__main__":
    s = SquareSum()
    s.add(1, 1)
    s.add(3, 2)
    s.add(5, 3)
    print(s.calc(1, 0)) # 5
    print(s.calc(1, -1)) # 2
    print(s.calc(0.5, 0.5)) # 0
    s.add(4, 2)
    print(s.calc(0.5, 0.5)) # 0.25