from ch7_source_code import LinkedQueue

def queue_merge(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():    # move remaining elements of S1 to S
        S.enqueue(S1.dequeue())
    while not S2.is_empty():    # move remaining elements of S2 to S
        S.enqueue(S2.dequeue())

if __name__ == '__main__':
    S1 = LinkedQueue()
    for i in range(10,20):
        S1.enqueue(i)

    S2 = LinkedQueue()
    for i in range(40,50):
        S2.enqueue(i)

    S = LinkedQueue()
    queue_merge(S1, S2, S)
    print(S.first(), len(S))    # LinkedQueue supports first and len operation
