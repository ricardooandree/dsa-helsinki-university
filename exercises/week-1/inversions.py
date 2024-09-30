""" Description:
You are given a list that consists of the numbers 1 ... n.
A pair of indices (i,j) is an inversion if i<j and the element at index i on the list is greater than the element at index j.
You may assume that n is at most 100.
In a file inversions.py, implement a function count that returns the total number of inversions in the list.
"""

""" Explanation:
The list [4,3,2,1] contains the inversions (0,1), (0,2), (0,3), (1,2), (1,3) and (2,3).
"""


def count(list):
    n = len(list)
    counter = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if list[i] > list[j]:
                counter += 1

    return counter

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12