#! /usr/bin/python3

import timeit


def list_comprehension(numbers):
    return [number for number in numbers if number % 2 == 0]


def filter_function(numbers):
    def is_even(number):
        return number % 2 == 0

    return filter(is_even, numbers)


def filter_function_with_lambda(numbers):
    return filter(lambda number: number % 2 == 0, numbers)


def truth_testing_with_filter(numbers):
    return filter(None, numbers)


def truth_testing_list_comprehension(numbers):
    return [number for number in numbers if number]


if __name__ == '__main__':
    elements = list(range(10) * 10)

    print("Elements: {0}".format(len(elements)))
    print("Filter: {0}".format(timeit.timeit("filter_function(elements)", setup="from __main__ import filter_function, elements ")))
    print("List Comprehension: {0}".format(timeit.timeit("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")))
    print("Truth testing with filter: {0}".format(timeit.timeit("truth_testing_with_filter(elements)", setup="from __main__ import truth_testing_with_filter, elements ")))
    print("Truth testing with List Comprehension: {0}".format(timeit.timeit("truth_testing_list_comprehension(elements)", setup="from __main__ import truth_testing_list_comprehension, elements")))

