""" Description:
You are given a string where each character is a bit (0 or 1). Your task is to change the string so that every bit is the same. What is the smallest number of changes needed?
You may assume that the string contains at most 100 characters.
In a file samebits.py implement a function count that returns the number of changes.
"""

""" Explanation:
Explanation: When the string is 01101, the best solution is to change both 0-bits into 1-bits. Thus two changes is needed in this case.
"""


def count(string):
    # TODO
    pass


if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4