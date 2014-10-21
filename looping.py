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
    elements = list(range(26 * 10))
    print("Elements: {0}".format(len(elements)))

    assert for_loop(elements) == optimised_for_loop(elements)
    assert optimised_for_loop(elements) == list_comprehension(elements)
    print("Self-test okay.")

    print("For Loop: {0}".format(timeit.timeit("for_loop(elements)", setup="from __main__ import for_loop, elements ")))
    print("Optimised For Loop: {0}".format(timeit.timeit("optimised_for_loop(elements)", setup="from __main__ import optimised_for_loop, elements ")))
    print("List Comprehension: {0}".format(timeit.timeit("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")))
