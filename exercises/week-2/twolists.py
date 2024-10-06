""" Description:
You are given two lists A and B both containing the numbers 1 ... n in some order. 
Your task is to count how many of the numbers 1 ... n occur earlier on the list A than on the list B. 
In this task, n can be large and an efficient algorithm is required. The time complexity should be O(n).
In a file twolists.py, implement a function count that returns the desired count.
"""


""" Explanation:
Explanation: In the first test, the numbers 2, 3 and 4 occur earlier on the list A than on the list B.
"""


def count(a, b):
    n = len(a)
    counter = 0
    b_index = [0] * (n + 1)

    for i in range(n):
        b_index[b[i]] = i

    for i in range(n):
        if i < b_index[a[i]]:
            counter += 1
    
    return counter


if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    #print(count([1,2,3,4], [1,2,3,4])) # 0
    #print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    #print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5