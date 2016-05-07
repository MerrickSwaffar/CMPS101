import numpy as np

#Brute force method for multiplying a matrix and a vector
def matmult(A,x):
    n = len(x)
    b = np.zeros(n)
    for i in range(0, n): #loop through the rows of the matrix
       for j in range(0, n): #loop through the columns of the matrix
            b[i] = b[i] + (A[i][j])*(x[j]) #perform multiplication and add to result vector
    return b
            
#Create a Hadamard matrix of size 2^k x 2^k
def hadmat(k):
   if k == 0: 
       return np.array([1]) #hadimard of size 1
   if k == 1:
       return np.array([[1, 1], [1, -1]])
   top = np.concatenate((hadmat(k-1), hadmat(k-1)), 1) #create top half 
   bottom = np.concatenate((hadmat(k-1), -1*hadmat(k-1)), 1) #create bottom half
   return np.concatenate((top, bottom), 0) #return the top concatenated with the bottom

#Recursive algorithm for multiplying a hadimard matrix by a vector 
def hadmatmult(H,x):
    n = len(x)
    if n <= 1: #base case. return H*x = x for size for hadamard of size 1
        return  x
    X = np.array_split(x,2) #split x in half
    h = H[0:n//2][0:n//2] #form H(n/2)
    p1 = hadmatmult(h, X[0]) #recursive calls to multiply
    p2 = hadmatmult(h, X[1])
    b1 = p1 + p2 #equation (2)
    b2 = p1 - p2 
    return np.concatenate((b1, b2), 0)

#Algorithm for multiplying a hadimard matrix by a vector without explicitly forming H(n/2)
def efficienthadmatmult(x):
    n = len(x)
    if n == 1: #base case. return H*x = x for size for hadamard of size 1
        return x
    X = np.array_split(x,2) #split x in half
    p1 = efficienthadmatmult(X[0]) #recursive calls to multiply
    p2 = efficienthadmatmult(X[1])
    b1 = p1 + p2 #equation (2)
    b2 = p1 - p2 
    return np.concatenate((b1, b2), 0)

#plotting code for question 5
'''
import matplotlib.pyplot as pl
import timeit
matmult_times = []
hadmatmult_times = [] 
  
for i in range(1, 13):
    x = np.random.randint(1, 1000, 2**i)
    H = hadmat(i)
    t = timeit.Timer(lambda: hadmatmult(H,x))
    hadmatmult_times.append(t.timeit(number=1))
    #t = timeit.Timer(lambda: matmult(H,x))
    #matmult_times.append(t.timeit(number=1))

pl.plot(np.arange(1,13), hadmatmult_times, np.arange(1,13), matmult_times)
pl.xlabel('input size')
pl.ylabel('time (seconds)')
pl.title('hadmatmult(blue) vs matmult(green)')
pl.show()        
'''
