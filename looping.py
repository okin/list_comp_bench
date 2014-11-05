#! /usr/bin/python3

import timeit


def list_comprehension(input):
    return list([element for element in elements])


def for_loop(input):
    data = []
    for element in elements:
        data.append(element)

    return list(data)


def optimised_for_loop(input):
    data = []
    appender = data.append
    for element in elements:
        appender(element)

    return list(data)


if __name__ == '__main__':
    elements = list(range(26 * 200))

    assert for_loop(elements) == optimised_for_loop(elements)
    assert optimised_for_loop(elements) == list_comprehension(elements)

    repeat_kwargs = {"number": 1000000, "repeat": 3}
    print("Creating a new list with {0} elements - lowest result of {number} calls repeated {repeat} times".format(len(elements), **repeat_kwargs))
    print("for-lop: {0:.2f}s".format(min(timeit.repeat("for_loop(elements)", setup="from __main__ import for_loop, elements ")), **repeat_kwargs))
    print("optimised for-loop: {0:.2f}s".format(min(timeit.repeat("optimised_for_loop(elements)", setup="from __main__ import optimised_for_loop, elements ")), **repeat_kwargs))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")), **repeat_kwargs))
