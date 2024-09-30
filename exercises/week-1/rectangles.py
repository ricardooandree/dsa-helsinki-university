""" Description:
You are given three rectangles whose sides are aligned with the horizontal and vertical axis.
Your task is to compute the total area covered by the rectangles. Overlapping regions are counted only once.
For example, in the following figure the area covered by the rectangles is 16. The figure corresponds to the example in the code template.

(rectangles.png)

You may assume that all the coordinates are integers in the range -10^9 ... 10^9.
Notice that going through all possible 1x1 rectangles one by one is too slow. You have to find a more efficient way to calculate the area.
Implement a function area(rec1, rec2, rec3) that returns the total area covered.
The function is given three tuples, each defining one rectangle.
Each tuple contains four integers x_1, y_1, x_2 and y_2: The top left corner is (x_1,y_1) and the bottom right corner is (x_2,y_2).
Implement the function in a file rectangles.py.
"""


def area_of_rectangle(rect1):
    # Rectangle area = (x2 - x1) * (y1 - y2)
    rect1_area = max(0, rect1[2] - rect1[0]) * max(0, rect1[1] - rect1[3])
    return rect1_area


def sum_area(rect1, rect2, rect3):
    return area_of_rectangle(rect1) + area_of_rectangle(rect2) + area_of_rectangle(rect3)


def intersection_rectangle(rect1, rect2):
    x1 = max(rect1[0], rect2[0])
    y1 = min(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = max(rect1[3], rect2[3])

    return (x1, y1, x2, y2)


def double_intersection_rectangle(rect1, rect2, rect3):
    intersection_rect12 = intersection_rectangle(rect1, rect2)
    intersection_rect123 = intersection_rectangle(intersection_rect12, rect3)

    return intersection_rect123


def area(rect1, rect2, rect3):
    # Rectangle = (x1, y1, x2, y2)
    # Mathematical formula: |A U B U C| = |A| + |B| + |C| - |A /\ B| - |B /\ C| - |A /\ C| + |A /\ B /\ C|
    total_area = sum_area(rect1, rect2, rect3)
    intersection_rect12_area = area_of_rectangle(intersection_rectangle(rect1, rect2))
    intersection_rect23_area = area_of_rectangle(intersection_rectangle(rect2, rect3))
    intersection_rect13_area = area_of_rectangle(intersection_rectangle(rect1, rect3))
    intersection_rect123 = area_of_rectangle(double_intersection_rectangle(rect1, rect2, rect3))

    return total_area - intersection_rect12_area - intersection_rect23_area - intersection_rect13_area + intersection_rect123


if __name__ == "__main__":
    rec1 = (-1, 1, 1, -1)
    rec2 = (0, 3, 2, 0)
    rec3 = (0, 2, 3, -2)
    print(area(rec1, rec2, rec3))  # 16
    rec1 = (2,-1,3,-3)
    rec2 = (0,2,3,0)
    rec3 = (-3,0,1,-1)
    print(area(rec1, rec2, rec3))  # 12
