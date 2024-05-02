from queue_merge import queue_merge
from ch7_source_code import LinkedQueue

def queue_merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                  # list is already sorted
    # divide
    S1 = LinkedQueue()          # or any other queue implementation
    S2 = LinkedQueue()
    while len(S1) < n // 2:     # move the first n//2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():     # move the rest to S2
        S2.enqueue(S.dequeue())
    # conquer (with recursion)
    queue_merge_sort(S1)
    queue_merge_sort(S2)
    # combine results
    queue_merge(S1, S2, S)            # merge sorted halves back into S

if __name__ == '__main__':
    S = LinkedQueue()
    for i in [34, 33, 22, 11, 9, 3, 6, 8]:
        S.enqueue(i)
    queue_merge_sort(S)
    print(S.first(), len(S))
