#! /usr/bin/python3

import timeit


def list_comprehension(input):
    return [element for element in elements]


def for_loop(input):
    data = []
    for element in elements:
        data.append(element)

    return data


def optimised_for_loop(input):
    data = []
    appender = data.append
    for element in elements:
        appender(element)

    return data


if __name__ == '__main__':
    elements = list(range(26 * 200))

    assert for_loop(elements) == optimised_for_loop(elements)
    assert optimised_for_loop(elements) == list_comprehension(elements)

    print("Creating a new list with {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements)))
    print("for-lop: {0:.2f}s".format(min(timeit.repeat("for_loop(elements)", setup="from __main__ import for_loop, elements "))))
    print("optimised for-loop: {0:.2f}s".format(min(timeit.repeat("optimised_for_loop(elements)", setup="from __main__ import optimised_for_loop, elements "))))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements"))))
