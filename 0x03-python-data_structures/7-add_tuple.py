#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    elem_1 = tuple_a[0] + tuple_b[0]
    elem_2 = tuple_a[1] + tuple_b[1]

    return (elem_1, elem_2)
