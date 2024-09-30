#!/usr/bin/python3

"""
contain the triangle
"""


def pascal_triangle(n):

    g_list = []
    if n <= 0:
        return g_list

    for x in range(n):
        list_added = [1] * (x + 1)
        if x > 1:
            for y in range(1, x):
                list_added[y] = g_list[x - 1][y - 1] + g_list[x - 1][y]
        g_list.append(list_added)

    return g_list
