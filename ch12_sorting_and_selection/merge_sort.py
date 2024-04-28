# implementation of recursive merge-sort algorithm for Python's list class
# using merge function defined in merge.py file

from merge import merge

def merge_sort(S):
    """Sort the element of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return              # list is already sorted
    # divide
    mid = n // 2
    S1 = S[:mid]            # copy of first half
    S2 = S[mid:]            # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results
    merge(S1, S2, S)        # merge sorted halves back into S


if __name__ == "__main__":
    S = [34, 11, 56, 2, 6, 98, 101]
    merge_sort(S)
    print(S)

