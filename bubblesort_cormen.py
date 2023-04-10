def bubblesort(A):
    for i in range(len(A)):
        for j in range (len(A)-1,i,-1):
            if A[j]<A[j-1]:
                temp_key=A[j]
                A[j]=A[j-1]
                A[j-1]=temp_key
        print(A)
    return A

A=[5,2,4,6,1,3,24,13,10,11,31,145,14]
print(bubblesort(A))

