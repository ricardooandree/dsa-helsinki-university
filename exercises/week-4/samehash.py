""" Description:
You are given a hash table size N. Your task is to find two strings that are assigned to the same location in the hash table using the Python hash function.
In other words, find two strings x and y such that hash(x) % N == hash(y) % N.
You may assume that N is at most 100. Your solution should be efficient for this case.
In a file samehash.py, implement a function find that returns the two strings as a pair.

Notice that the function hash changes each time the Python interpreter is started. This means that the function must return different strings at different executions.
"""


def find(N):
    # TODO
    pass

if __name__ == "__main__":
    print(find(42)) # esim. ('abc', 'aybabtu')