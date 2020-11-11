# from Real Python - Easier Interview Question
from math import floor


def majority_element_indexes(lst):
    """/home/gseverina/repos/codility
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    """
    return [i for i, x in enumerate(lst) if lst.count(x) > floor(len(lst) / 2)]


if __name__ == "__main__":
    assert majority_element_indexes([1, 1, 2]) == [0, 1]
    assert majority_element_indexes([1, 2]) == []
    assert majority_element_indexes([]) == []

