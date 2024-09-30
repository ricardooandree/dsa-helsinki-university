""" Description:
Your task is to find out how long is the shortest string that forms the given string when repeated.
For example, when the input string is abcabcabcabc, the shortest repeating string is abc.

The string consists of the characters a–z and contains at most 100 characters.

In a file repeat.py, implement a function find that returns the length of the shortest repeating string.
"""


def find(string):
    pattern = ""

    for char in string:
        pattern += char

        if pattern * (len(string) // len(pattern)) == string:
            return len(pattern)


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7