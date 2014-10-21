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
    print("Elements: {0}".format(len(elements)))

    assert map_function(elements) == map_function_with_lambda(elements)
    assert map_function_with_lambda(elements) == list_comprehension(elements)
    print("Self-test okay.")

    print("Map function: {0}".format(timeit.timeit("map_function(elements)", setup="from __main__ import map_function, elements ")))
    print("Map function with lambda: {0}".format(timeit.timeit("map_function_with_lambda(elements)", setup="from __main__ import map_function_with_lambda, elements ")))
    print("List Comprehension: {0}".format(timeit.timeit("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")))

