#! /usr/bin/python3

import timeit


def filter_function(numbers):
    def is_even(number):
        return number % 2 == 0

    return filter(is_even, numbers)


def filter_function_with_lambda(numbers):
    return filter(lambda number: number % 2 == 0, numbers)


def list_comprehension(numbers):
    return [number for number in numbers if number % 2 == 0]


def truth_testing_with_filter(numbers):
    return filter(None, numbers)


def truth_testing_with_filter_and_builtin(numbers):
    return filter(bool, numbers)


def truth_testing_with_lambda_and_filter(numbers):
    return filter(lambda x: x, numbers)


def truth_testing_list_comprehension(numbers):
    return [number for number in numbers if number]


def unique_items_with_set(elements):
    return set(elements)


def unique_items_with_set_and_list(elements):
    return list(set(elements))


def unique_items_with_for_loop(elements):
    new = []
    for element in elements:
        if element not in new:
            new.append(element)
    return new


if __name__ == '__main__':
    elements = list(range(26) * 200)

    assert list(filter_function(elements)) == list(filter_function_with_lambda(elements))
    assert list(filter_function_with_lambda(elements)) == list(list_comprehension(elements))
    assert list(truth_testing_with_filter(elements)) == list(truth_testing_with_lambda_and_filter(elements))
    assert list(truth_testing_with_filter(elements)) == list(truth_testing_with_filter_and_builtin(elements))
    assert list(truth_testing_with_lambda_and_filter(elements)) == list(truth_testing_list_comprehension(elements))
    assert list(unique_items_with_set(elements)) == unique_items_with_set_and_list(elements)  # A small cheat because we are only interested in the contents
    assert list(unique_items_with_set_and_list(elements)) == list(unique_items_with_for_loop(elements))

    print("Filtering a list of {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements)))
    print("filter(): {0:.2f}s".format(min(timeit.repeat("filter_function(elements)", setup="from __main__ import filter_function, elements "))))
    print("filter() and lambda: {0:.2f}s".format(min(timeit.repeat("filter_function_with_lambda(elements)", setup="from __main__ import filter_function_with_lambda, elements "))))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("list_comprehension(elements)", setup="from __main__ import list_comprehension, elements"))))

    print("Truth testing with a list of {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements)))
    print("filter(): {0:.2f}s".format(min(timeit.repeat("truth_testing_with_filter(elements)", setup="from __main__ import truth_testing_with_filter, elements "))))
    print("filter() and lambda: {0:.2f}s".format(min(timeit.repeat("truth_testing_with_lambda_and_filter(elements)", setup="from __main__ import truth_testing_with_lambda_and_filter, elements "))))
    print("filter() and builtin: {0:.2f}s".format(min(timeit.repeat("truth_testing_with_filter_and_builtin(elements)", setup="from __main__ import truth_testing_with_filter_and_builtin, elements "))))
    print("list comprehension: {0:.2f}s".format(min(timeit.repeat("truth_testing_list_comprehension(elements)", setup="from __main__ import truth_testing_list_comprehension, elements"))))

    print("Creating a list with of unique elements with a list of {0} elements - lowest result of 1000000 calls repeated 3 times".format(len(elements)))
    print("set(): {0:.2f}s".format(min(timeit.repeat("unique_items_with_set(elements)", setup="from __main__ import unique_items_with_set, elements"))))
    print("list(set()): {0:.2f}s".format(min(timeit.repeat("unique_items_with_set_and_list(elements)", setup="from __main__ import unique_items_with_set_and_list, elements"))))
    print("for-loop: {0:.2f}s".format(min(timeit.repeat("unique_items_with_for_loop(elements)", setup="from __main__ import unique_items_with_for_loop, elements"))))
