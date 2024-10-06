""" Description: 
Your task is to count how many numbers occur on a given list.
An element of the list can be a list that may in turn contain other lists, which may contain other lists etc.
In each list, every element is either a list or a number.
You may assume that the total count of numbers is at most 100 and that there are at most 100 levels of nested lists.
In a file nestedlist.py, implement a function count that returns the desired count.
"""


def count(my_list):
    result = 0

    for elem in my_list:
        if isinstance(elem, list):
            result += count(elem)
        else:
            result += 1
    return result

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8