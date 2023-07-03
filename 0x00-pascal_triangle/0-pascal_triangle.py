#!/usr/bin/python3
"""returns a pascal triangle"""


def pascal_triangle(n):
    """
    Function that returns a list of integers using a pascal triangle format.
    """

    if n <= 0:
        # returns an empty list
        return []

    ps = [[1]]
    if n == 1:
        return ps

    for i in range(1, n):
        left = -1
        right = 0
        ps_in = []
        for j in range(i + 1):
            num = 0
            if left > -1:
                num += ps[i - 1][left]
            if right < i:
                num += ps[i - 1][right]
            left += 1
            right += 1
            ps_in.append(num)
        ps.append(ps_in)
    return ps
