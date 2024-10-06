""" Description:
Create a list that contains the numbers 1 ... n and where each pair of consecutive numbers has a different sum. Any list satisfying the conditions is acceptable.
You may assume that n is in the range 1 ... 100.
In a file sumdiff.py, implement a function create that returns the required list.
"""


""" Explanation:
Explanation: In the code template example [3,1,6,2,4,5], the sums of pairs are 4, 7, 8, 6 and 9.
Since all the sums are different, the solution is valid. For example the solution [1,5,2,6,4,3] would not be valid, because 5+2=7 and 4+3=7.
"""


def create(n):
    if n <= 1:
        return [n]
    return [i + 1 for i in range(n)]

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]