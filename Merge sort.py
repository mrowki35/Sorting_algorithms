#MErge sort

merge_sort_calls = 1
merge_calls = 0


def Merge(A, p, q, r):
    global merge_calls
    merge_calls += 1

    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1







def Merge_Sort(A, p, r):
    global merge_sort_calls
    merge_sort_calls += 1

    if p < r:
        
        q=((p+r) // 2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        Merge(A, p, q, r)





A = [5,2,4,7,1,3,2,6]
Merge_Sort(A,0,len(A)-1)
print(merge_sort_calls, merge_calls)
print(A)

