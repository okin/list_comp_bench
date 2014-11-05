#! /usr/bin/python3

import string
import timeit


def list_comprehension(elements):
    return list([element.upper() for element in elements])


def map_function(elements):
    def uppercase(element):
        return element.upper()

    return list(map(uppercase, elements))


def map_function_with_lambda(elements):
    return list(map(lambda element: element.upper(), elements))


if __name__ == '__main__':
    elements = list(string.ascii_lowercase * 200)

    assert map_function(elements) == map_function_with_lambda(elements)
    assert map_function_with_lambda(elements) == list_comprehension(elements)

    repeat_kwargs = {"number": 1000000, "repeat": 3}
    print("Mapping a function on an list with {0} elements - lowest result of {number} calls repeated {repeat} times".format(len(elements), **repeat_kwargs))
    print("map(): {0:.2f}s".format(min(timeit.repeat("map_function(elements)", setup="from __main__ import map_function, elements ", **repeat_kwargs))))
    print("map() and lambda: {0:.2f}s".format(min(timeit.repeat("map_function_with_lambda(elements)", setup="from __main__ import map_function_with_lambda, elements", **repeat_kwargs))))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements", **repeat_kwargs))))
