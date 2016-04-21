import numpy as np

#sorting function implementing the selection sort algorithm
def selectionsort(A):
    #iterate through each element of the array
    for i in range(0, len(A)):
        min = A[i]
        min_index = i
        #identify the minimum element in A[i,...,n] 
        for j in range(i, len(A)):
            if A[j] < min:
                min = A[j]
                min_index = j
        #swap A[i] with the minimum of A[i,...,n]
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp
    return A

#sorting function implementing the insertion sort algorithm
def insertionsort(A):
    if len(A) <= 1:
        return A
    #iterate through each element of the array
    for i in range(0, len(A)):
        j = i
        #iterate from j to 1, swaping A[j] with A[j-1] if they are out of order
        while j > 0 and A[j-1] > A[j]:
            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp
            j = j - 1
    return A

#sorting function implementing the merge sort algorithm         
def mergesort(A):
    n = len(A)
    #base case. if n = 0 or 1, return trivially sorted array
    if n <= 1:
        return A
    #split the array into left and right
    L = A[0:n//2]
    R = A[n//2:n]
    #recursively call mergesort on left and right
    L_sort = mergesort(L)
    R_sort = mergesort(R)
    #merge the two sorted arrays together and return a single sorted array
    return merge(L_sort, R_sort)

#merge two sorted arrays into one sorted array
def merge(L, R):
    M = np.array([], dtype=int)
    i = j = 0
    #while there are still elements in L and R, put the least element into M
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            M = np.append(M, L[i])
            i = i+1
        else: 
            M = np.append(M, R[j])
            j = j+1
    #put any remaining elements of L or R into M
    if L.any:
        M = np.append(M, L[i:])
    if R.any:
        M = np.append(M, R[j:])
    #return the result of the merge, M
    return M

