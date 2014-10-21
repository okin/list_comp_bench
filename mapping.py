#! /usr/bin/python3

import string
import timeit


def list_comprehension(elements):
    return [element.upper() for element in elements]


def map_function(elements):
    def uppercase(element):
        return element.upper()

    return map(uppercase, elements)


def map_function_with_lambda(elements):
    return map(lambda element: element.upper(), elements)


if __name__ == '__main__':
    elements = list(string.ascii_lowercase * 10)

    assert map_function(elements) == map_function_with_lambda(elements)
    assert map_function_with_lambda(elements) == list_comprehension(elements)

    print("Mapping a function on an list with {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements)))
    print("map(): {0:.2f}s".format(min(timeit.repeat("map_function(elements)", setup="from __main__ import map_function, elements "))))
    print("map() and lambda: {0:.2f}s".format(min(timeit.repeat("map_function_with_lambda(elements)", setup="from __main__ import map_function_with_lambda, elements "))))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements"))))
