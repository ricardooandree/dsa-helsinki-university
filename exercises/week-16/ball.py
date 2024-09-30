""" Description:
A ball is participated by n students from Kumpula and n students from Viikki. The students of each campus are numbered 1,2,...,n.
Each dancing pair has one student from Kumpula and one from Viikki, and you know all pairs that are willing to dance with each other.
Each student can belong to at most one dancing pair. What is the maximum number of pairs that can be formed?
Implement a class Ball with the following methods:

add_pair declares that a student a from Kumpula and a student b from Viikki are willing to dance with each other
calculate returns the maximum number of dancing pairs

Implement the class in a file ball.py according to the following template.
"""


class Ball:
    def __init__(self, n):
        # TODO
        pass

    def add_pair(self, a, b):
        # TODO
        pass

    def calculate(self):
        # TODO
        pass

if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1, 2)
    print(b.calculate()) # 1
    b.add_pair(1, 3)
    b.add_pair(3, 2)
    print(b.calculate()) # 2