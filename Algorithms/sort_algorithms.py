"""Module to hold different sort algorithms.Merge, Quick, Bucket, Heap, Counting."""


"""
To hold:
    Merge
    Quick
    Bucket
    Heap
    Counting
"""

def sort(array, method='quick'):
    """Generalized sort algorithm that allows for type change."""
    method = method.lower()
    sort_types = ['quick', 'merge', 'bucket', 'heap', 'counting']
    while method not in sort_types:
        print "Method entered must be one of: "
        print '\n\t'.join(sort_types.title())
        method = input().lower()
    if method is 'quick':
        return quicksort(array)
    else:
        print 'FUNCTION NOT WRITTEN YET'


def quicksort(array):
    """Recursive quicksort algorithm."""
    # Base case
    if len(array) <= 1:
        return array
    pivot = array[len(array) / 2]  # Point in array to pivot around
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)
