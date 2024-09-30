""" Description:
Your task is to design a class that supports adding courses and their prerequisite relations, and finding a way to take the courses in an order that satisfies the requisites.

Implement a class CoursePlan with the following methods:

add_course adds a course with the given name
add_requisite adds a prerequisite
find_order returns a satisfactory course plan as a list (or None if there is no satisfactory plan)

Implement the class in a file courseplan.py according to the following template:
"""


class CoursePlan:
    def __init__(self):
        # TODO
        pass

    def add_course(self, course):
        # TODO
        pass

    def add_requisite(self, course1, course2):
        # TODO
        pass

    def find_order(self):
        # TODO
        pass

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find_order()) # None