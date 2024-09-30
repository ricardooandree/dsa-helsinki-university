""" Description:
A network has n computers and there are connecting links between them. Each link can be used for sending a certain number of bits per second from one computer to the other.
Your task is to find out what is the maximum number of bits per second that can be send from a given computer to another.
Implement a class Download with the following methods:

add_link adds a connecting link from a computer a to a computer b capable of moving x bits per second
calculate returns the maximum bit rate from a computer a
to a computer b

Implement the class in a file download.py according to the following template.
"""


class Download:
    def __init__(self, n):
        # TODO
        pass

    def add_link(self, a, b, x):
        # TODO
        pass

    def calculate(self, a, b):
        # TODO
        pass

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1, 4)) # 0
    d.add_link(1, 2, 5)
    d.add_link(2, 4, 6)
    d.add_link(1, 4, 2)
    print(d.calculate(1, 4)) # 7
    d.add_link(1, 3, 4)
    d.add_link(3, 2, 2)
    print(d.calculate(1, 4)) # 8