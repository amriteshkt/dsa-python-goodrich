def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)

    if m == 0: return 0             # trivial search for empty string

    last = {}                       # lookup table for function last(c)
    # if c is in P, last(c) is the index of the last occurrence of c in P
    # otherwise, we conventionally define last(c) = -1

    for k in range(m):
        last[P[k]] = k              # later occurrence overwrites

    # align end of pattern at index m-1 of text
    i = m-1                         # an index into T
    k = m-1                         # an index into P
    while i < n:
        if T[i] == P[k]:            # a matching character
            if k == 0:
                return i            # examine previous character
            else:
                i -= 1              # examine previous character
                k -= 1              # of both T and P
        else:
            j = last.get(T[i], -1)  # last(T[i]) is -1 if not found
            i += m - min(k, j+1)    # case analysis for jump step
            k = m - 1               # restart at end of pattern

    return -1

if __name__ == '__main__':
    T = 'abacaabadcabacabaabb'
    P = 'abacab'
    print(find_boyer_moore(T, P))
