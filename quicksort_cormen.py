PARTITION_calls=0
quicksort_calls=1



def PARTITION(A,p,r):
    global PARTITION_calls
    PARTITION_calls=PARTITION_calls + 1
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j] <= x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
    


def quicksort(A,p,r):
    global quicksort_calls
    quicksort_calls = quicksort_calls + 1
    if p<r:
        q=PARTITION(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A

A=[5,2,4,6,1,3,24,13,10,11,31,145,14,6]


print(quicksort(A,0,len(A)-1))
print(PARTITION_calls,quicksort_calls)
