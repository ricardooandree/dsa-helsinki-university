""" Description:
You are given a list that contains n integers.
Consider a process, where at each step you find the two smallest integers on the list, remove both from the list, and add the sum of the two numbers minus one to the end of the list.
This continues until the list contains only a single number. What is this number?
Your task is to create an efficient algorithm that determines that last number for a given list. The time complexity of the algorithm should be O(n).
In a file lastnumber.py, implement a function find that returns the desired number.
"""


""" Explanation:
Explanation: Given the list [1,2,3,4], you first remove the numbers 1 and 2 and add the number 2. Now the list is [3,4,2].
Then you remove the numbers 3 and 2 and add the number 4, obtaining the list [4,4]. Finally, you remove the numbers 4 and 4 and add the number 7, obtaining the list [7].
"""


def find(t):
    # TODO
    pass

if __name__ == "__main__":
    print(find([1,2,3,4])) # 7
    print(find([1,1,1])) # 1
    print(find([5,1,1,7,9,1,2])) # 20