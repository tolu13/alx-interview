#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    # Initialize an empty resulting array
    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li + 1):
            if col < li:
                if col == 0:
                    # The first column is always set to 1
                    pascal[li].append(1)
                else:
                    prev_row = pascal[li - 1]
                    current_val = prev_row[col] + prev_row[col - 1]
                    pascal[li].append(current_val)
            elif col == li:
                # The diagonal is always set to 1
                pascal[li].append(1)

    return pascal
