""" Description:
Initially the contents of the list are [1,2,3,...,n]. In each step, you take the first two elements of the list and move them to the end of the list in reverse order. What is the first element of the list after k steps?
For example, when n=4 and k=3, the list changes as follows:
[1,2,3,4] -> [3,4,2,1] -> [2,1,4,3] -> [4,3,1,2]

In this case, the first element of the list is 4.
The time complexity of the algorithm should be O(n+k).
In a file fliptwo.py, implement a function solve that returns the first element after k steps.
"""


def solve(n,k):
    # TODO
    pass

if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875