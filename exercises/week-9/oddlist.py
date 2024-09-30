""" Description:
How many ways can you construct a list from the numbers 1 ... n so that all sums of adjacent pairs are distinct and so that the first number is x?
You may assume that 1 <= n <= 8 and that 1 <= x <= n. The algorithm should be efficient in all these cases.
In a file oddlist.py, implement a function count that returns the desired count.
"""


""" Explanation:
Explanation: When n=4 and x=2, the answer is 4, because the lists are [2,1,3,4], [2,1,4,3], [2,4,1,3] and [2,4,3,1].
"""


def count(n, x):
    # TODO
    pass

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830