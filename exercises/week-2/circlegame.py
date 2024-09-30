""" Description:
There is a circle of n players numbered 1,2,\dots,n. The players take turns in order around the circle, and every second player leaves the circle until the circle is empty. Your task is to determine the order in which the players leave.
You may assume that n is in the range 1 \dots 100.
In a file circlegame.py, implement a function create that returns the order.
"""


def create(n):
    # TODO
    pass

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]