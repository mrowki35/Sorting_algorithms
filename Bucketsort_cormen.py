def Bucketsort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        bucket_index = n * A[i]
        B[bucket_index].append(A[i])
    for i in range(n):
        insertion_sort(B[i])
    result = []
    for i in range(n):
        result = B[i] + result