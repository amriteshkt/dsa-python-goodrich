def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(T), len(P)       # introduce convenient notations
    for i in range(n-m+1):      # try every potential starting index within T
        k = 0
        while k < m and T[i+k] == P[k]:     # kth character of P matches
            k += 1
        if k == m:              # if we reached the end of patter,
            return i            # substring T[i:i+m] matches P
    return -1

if __name__ == '__main__':
    print(find_brute('lenovophone', 'vop'))
