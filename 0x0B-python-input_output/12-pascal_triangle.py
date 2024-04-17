#!/usr/bin/python3
'''pascal_triangle function module'''


def pascal_triangle(n):
    '''define Pascal's Triange of size n.
    Args:
        n: size
    Returns:
        a list of lists of integers representing the triangle
    '''

    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        tr = t[-1]
        tmp = [1]
        for i in range(len(tr) - 1):
            tmp.append(tr[i] + tr[i+1])
        tmp.append(1)
        t.append(tmp)
    return t
