# an implementation of merge operation for Python's array-based list class

def merge(S1, S2, S):
    """Merge two sorted Python lists S1 ans S2 into properly sized list S."""
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]  # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]  # copy jth element of S2 as next item of S
            j += 1

if __name__ == "__main__":
    S1 = [23, 45, 56, 89, 90]   # S1 ans S2 must be sorted beforehand
    S2 = [40, 99, 102]
    S = [None]*(len(S1)+len(S2))
    merge(S1,S2,S)
    print(S)

