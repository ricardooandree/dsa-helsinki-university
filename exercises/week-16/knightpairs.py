""" Description:
You are given a chess board of 8 * 8 squares. Each square is either empty or contains a knight. In the description of the board, the character . means an empty square and the character * means a knight.
Your task is to form as many pairs of knights as possible. The knights in a pair must attack each other, and each knight can belong to at most one pair. 
Two knights attack each other if either their horizontal or their vertical distance is 1 and the other distance is 2 (as in the rules of chess).
In a file knightpairs.py, implement a function count that returns the maximum number of pairs.
"""


def count(r):
    # TODO
    pass

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3