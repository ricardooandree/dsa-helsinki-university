""" Description:
You are given a bit string that consists of the characters 0 and 1. How many ways can you choose two positions in the bit string so that each position has the same bit?
The time complexity of the algorithm should be O(n).
In a file samebit.py, implement a function count that returns the desired count.
"""


def count(s):
    # TODO
    pass

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46