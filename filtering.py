#! /usr/bin/python3

import timeit


def filter_function(numbers):
    def is_even(number):
        return number % 2 == 0

    return list(filter(is_even, numbers))


def filter_function_with_lambda(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


def list_comprehension(numbers):
    return list([number for number in numbers if number % 2 == 0])


def truth_testing_with_filter(numbers):
    return list(filter(None, numbers))


def truth_testing_with_filter_and_builtin(numbers):
    return list(filter(bool, numbers))


def truth_testing_with_lambda_and_filter(numbers):
    return list(filter(lambda x: x, numbers))


def truth_testing_list_comprehension(numbers):
    return list([number for number in numbers if number])


def unique_items_with_set(elements):
    return list(set(elements))


def unique_items_with_for_loop(elements):
    new = []
    for element in elements:
        if element not in new:
            new.append(element)
    return list(new)


if __name__ == '__main__':
    elements = list(range(26)) * 200

    assert filter_function(elements) == filter_function_with_lambda(elements)
    assert filter_function_with_lambda(elements) == list_comprehension(elements)
    assert truth_testing_with_filter(elements) == truth_testing_with_lambda_and_filter(elements)
    assert truth_testing_with_filter(elements) == truth_testing_with_filter_and_builtin(elements)
    assert truth_testing_with_lambda_and_filter(elements) == truth_testing_list_comprehension(elements)
    assert unique_items_with_set(elements) == unique_items_with_for_loop(elements)

    repeat_kwargs = {"number": 1000000, "repeat": 3}
    print("Filtering a list of {0} elements - lowest result of {number} calls repeated {repeat} times".format(len(elements), **repeat_kwargs))
    print("filter(): {0:.2f}s".format(min(timeit.repeat("filter_function(elements)", setup="from __main__ import filter_function, elements ")), **repeat_kwargs))
    print("filter() and lambda: {0:.2f}s".format(min(timeit.repeat("filter_function_with_lambda(elements)", setup="from __main__ import filter_function_with_lambda, elements ")), **repeat_kwargs))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements")), **repeat_kwargs))

    print("Truth testing with a list of {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements), **repeat_kwargs))
    print("filter(): {0:.2f}s".format(min(timeit.repeat("truth_testing_with_filter(elements)", setup="from __main__ import truth_testing_with_filter, elements ")), **repeat_kwargs))
    print("filter() and lambda: {0:.2f}s".format(min(timeit.repeat("truth_testing_with_lambda_and_filter(elements)", setup="from __main__ import truth_testing_with_lambda_and_filter, elements ")), **repeat_kwargs))
    print("filter() and builtin: {0:.2f}s".format(min(timeit.repeat("truth_testing_with_filter_and_builtin(elements)", setup="from __main__ import truth_testing_with_filter_and_builtin, elements ")), **repeat_kwargs))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("truth_testing_list_comprehension(elements)", setup="from __main__ import truth_testing_list_comprehension, elements")), **repeat_kwargs))

    print("Creating a list with of unique elements with a list of {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements), **repeat_kwargs))
    print("set(): {0:.2f}s".format(min(timeit.repeat("unique_items_with_set(elements)", setup="from __main__ import unique_items_with_set, elements")), **repeat_kwargs))
    print("for-loop: {0:.2f}s".format(min(timeit.repeat("unique_items_with_for_loop(elements)", setup="from __main__ import unique_items_with_for_loop, elements")), **repeat_kwargs))
