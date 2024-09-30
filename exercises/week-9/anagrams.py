""" Description:
An anagram of a string contains the characters of the string in some order. Your task is to construct all the anagrams of a given string.
You may assume that the string consists of the characters a–z and contains at most 8 characters. The algorithm should be efficient in all of these cases.
In a file anagrams.py, implement a function create that returns a sorted list of the anagrams.
"""


def create(s):
    # TODO
    pass

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260