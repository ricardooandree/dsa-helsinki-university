""" Description:
Implement a class with the following methods:

push_first(x): add the number x to the beginning of the list
push_last(x): add the number x to the end of the list
pop_first(): return and remove the element at the beginning of the list
pop_last(): return and remove the element at the end of the list
flip(): reverse the contents of the list

Each method should work in O(1) time.
In a file fliplist.py, implement a class FlipList according to the following template.
"""


class FlipList:
    def push_first(self, x):
        # TODO
        pass

    def push_last(self, x):
        # TODO
        pass

    def pop_first(self):
        # TODO
        pass

    def pop_last(self):
        # TODO
        pass

    def flip(self):
        # TODO
        pass

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3