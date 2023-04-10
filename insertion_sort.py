def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
        print(A)
    return A

A=[5,2,4,6,1,3,24,13,10,11,31,145,14]

print(insertion_sort(A))