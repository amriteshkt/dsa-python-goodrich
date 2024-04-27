def inplace_quick_sort(S, low, high):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if low >= high:
        return              # range is trivially sorted
    pivot = S[high]         # last element of range is pivot
    left = low              # will scan rightward
    right = high - 1        # will scan leftward

    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:   # scan didn't strictly cross
            S[left], S[right] = S[right], S[left]   # swap values
            left, right = left + 1, right - 1       # shrink range

    # put pivot into its final place (currently marker by left index)
    S[left], S[high] = S[high], S[left]

    # make recursive calls
    inplace_quick_sort(S, low, left-1)
    inplace_quick_sort(S, left + 1, high)

if __name__ == '__main__':
    S = [85, 24, 63, 45, 17, 31, 96, 50]
    low = 0
    high = len(S) - 1
    inplace_quick_sort(S, low, high)
    print(S)
