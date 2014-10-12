#! /usr/bin/python3

import timeit


def list_comprehension(input):
    data = [element for element in elements]


def for_loop(input):
    data = []
    for element in elements:
        data.append(element)


def optimised_for_loop(input):
    data = []
    appender = data.append
    for element in elements:
        appender(element)


elements = list(range(100))

print("Elements: {0}".format(len(elements)))
print("For Loop: {0}".format(timeit.timeit("for_loop(elements)", setup="from __main__ import for_loop, elements ")))
print("Optimised For Loop: {0}".format(timeit.timeit("optimised_for_loop(elements)", setup="from __main__ import optimised_for_loop, elements ")))
print("List Comprehension: {0}".format(timeit.timeit("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")))