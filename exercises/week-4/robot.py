""" Description:
Initially the robot is located in the square (0,0). The robot will then move according to a given move sequence step by step. The move sequence consists of the characters U (up), D (down), L (left) and R (right). How many different squares does the robot visit?
The time complexity of the algorithm should be O(n).
In a file robot.py, implement a function count that is given the robot move sequence and that returns the number of different squares.
"""


def count(s):
    # TODO
    pass

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2