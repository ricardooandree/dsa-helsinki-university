""" Description:
Your task is to count how many ways can you place k queens on an n*n chess board so that no two queens attack each other?
You may assume that 1 <= n <= 8 and that 1 <= k <= 3. Your solution should be efficient in all of these cases.
In a file queens.py, implement a function count that returns the desired count.
"""


def count(n, k):
    # TODO
    pass

if __name__ == "__main__":
    print(count(2, 1)) # 4
    print(count(2, 2)) # 0
    print(count(5, 3)) # 204
    print(count(7, 1)) # 49
    print(count(7, 2)) # 700
    print(count(7, 3)) # 3628