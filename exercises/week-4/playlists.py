""" Description:
You are given a play list, where each song is represented by an integer. Your task to find out how many sublists of the play list contain no song twice.
The time complexity of the algorithm should be O(n).
In a file playlists.py, implement a function 'count` that returns the number of sublists.
"""


def count(t):
    # TODO
    pass

if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24