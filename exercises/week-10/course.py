""" Description:
A course consists of 8 weeks, each of which has 8 tasks. You pass the course, if you complete at least 5 tasks each week.
How many ways can you pass the course so that you complete a total of x tasks? Two ways of passing the course are considered different, if the lists of completed tasks in the order of completion are different.
You may assume that 1 <= x <= 100. The algorithm should be efficient in all these cases. The code must compute the results and not just return precomputed results.
In a file course.py, implement a function count that returns the number of ways to complete the course.
"""

""" Explanation:
Explanation: When x=40, exactly 5 tasks must be completed each week.
The tasks can be completed in 40! different orders and the tasks for each week can be chosen in {8 5} ways.
Thus answer is 40! * {8 5}^8. When x=64, all tasks are completed and thus the answer is 64!.
"""


def count(x):
    # TODO
    pass

if __name__ == "__main__":
    print(count(40)) # 78913132667888442497725132524762783866832203758436352000000000
    print(count(55)) # 320424698352073967965876852452014215914220727801318938295395908593909760000000000000
    print(count(64)) # 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000
    print(count(100)) # 0