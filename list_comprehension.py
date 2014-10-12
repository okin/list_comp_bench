#! /usr/bin/python3

import timeit


def list_comprehension(input):
    data = [element for element in elements]


def for_loop(input):
    data = []
    for element in elements:
        data.append(element)


elements = list(range(100))

print("List Comprehension")
print(timeit.timeit("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements"))
print("For Loop")
print(timeit.timeit("for_loop(elements)", setup="from __main__ import for_loop, elements "))
