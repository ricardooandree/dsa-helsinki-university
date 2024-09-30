""" Description:
You are given a list that contains the numbers 1 \dots n in some order. Your task is to sort the list using two commands:

SWAP: swaps the first two elements of the list
MOVE: moves the first element of the list to the end of the list

Design an algorithm that constructs a sequence of commands such that executing the the sequence sorts the list. The algorithm may return any valid solution that contains no more than n^3 commands.
In a file swapmove.py, implement a function solve that returns the sequence of commands as a list. Each element of the answer should be either the string SWAP or the string MOVE."""


""" Explanation:
Explanation: The list [1,3,2] can be sorted by executing first the command SWAP, resulting in the list [3,1,2], and then the command MOVE, resulting in the list [1,2,3].
"""


def solve(t):
    # TODO
    pass

if __name__ == "__main__":
    print(solve([1, 2])) # e.g. []
    print(solve([2, 1])) # e.g. [SWAP]
    print(solve([1, 3, 2])) # e.g. [SWAP, MOVE]
    print(solve([3, 2, 1])) # e.g. [MOVE, SWAP]
    print(solve([2, 3, 4, 1])) # e.g. [MOVE, MOVE, MOVE]