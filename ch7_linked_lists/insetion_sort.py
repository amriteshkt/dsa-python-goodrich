from positional_list import PositionalList



def insertion_sort(L):
    """We try to sort positional list which is formed by double linked list,
    in the same way as we sort array-based sequence.
    """
    if len(L) > 1:
        marker = L.first()  # Position (Position class) of first element
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():  # using element of Position class
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

def insertion_sort_older(L):
    """Insertion sort using Python List."""
    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            k = i
            while L[k] < L[k-1] and k >= 1:
                temp = L[k-1]
                L[k-1] = L[k]
                L[k] = temp
                k -= 1

def another_positional_list_sort(L):
    """Sorting the positional list."""
    if len(L) > 1:
        position = L.first()
        position = L.after(position)
        while position:
            if position.element() < L.before(position).element():
                walk = position
                while walk != L.first() and walk.element() < L.before(walk).element():
                    temp = walk.element()
                    z = L.replace(L.before(walk), temp)
                    L.replace(walk, z)
                    walk = L.before(walk)
            position = L.after(position)
            # after traversing whole list, we reach trailer, then L.after(position) return none
            # see after() method of PositionalList

if __name__ == "__main__":
    # test for positional list.
    lst = PositionalList()
    
    for i in [23,12,34,56,11,23]:
        lst.add_first(i)
    print("list before sorting: ", lst)
    insertion_sort(lst)
    print("list after sorting: ", lst)

    # test for python list.
    lst1 = [23,12,34,56,11,23]
    insertion_sort_older(lst1)
    print(lst1)

    # test for positional list.
    lst2 = PositionalList()
    
    for i in [23,12,34,56,11,23]:
        lst2.add_first(i)
    print("list before sorting: ", lst2)
    another_positional_list_sort(lst2)
    print("list after sorting: ", lst2)
    