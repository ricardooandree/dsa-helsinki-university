""" Description:
The following function given in the course material computes the number of balanced parenthesis sequences:
"""


def count_sequences(n, result={}):
    if n == 0:
        return 1
    if n not in result:
        count = 0
        for i in range(2, n + 1, 2):
            count += count_sequences(i - 2) * \
                     count_sequences(n - i)
        result[n] = count
    return result[n]


""" Description:
Modify the function so that it computes the result using the same logic but using loops instead of recursion.
Verify that the modified function produces the same answer for the case n=100.
In this task, you get a point automatically, when you fill in your implementation and press the submit button.

Notice that the above function uses a different logic than the function that was similarly modified in the course material.
The non-recursive function in the course material is not a valid solution here.
"""

# TODO Modified function:

