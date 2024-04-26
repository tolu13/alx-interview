def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list: A list of lists representing Pascal's triangle.

    Raises:
    - ValueError: If n is less than or equal to 0.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
