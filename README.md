list_comp_bench
===============

Benchmarks for various ways of working with list comprehension.

Working in Python 2 and 3.
To achieve this I needed to somehow consume the iterators that Python 3 produces and therefore convert the created iterables to a list.
This alters the "pure" results but because the overhead is applied to all scripts the results still should be comparable.
