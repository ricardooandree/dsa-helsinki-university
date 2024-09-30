""" Description:
The robot moves as in the earlier exercise this week, but now it repeats the same move sequence k times. How many different squares does the robot visit?
You may assume that the move sequence has at most 100 moves, and that k is in the range 1 \dots 10^9. The algorithm should be efficient within these limits.
In a file longroute.py, implement a function count that returns the square count given the move sequence and the repeat count.
"""


def count(s,k):
    # TODO
    pass

if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4