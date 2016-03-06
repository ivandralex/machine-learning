import numpy as np

X = np.random.normal(loc=1, scale=10, size=(1000, 50))
#print X


m = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_norm = ((X - m)  / std)

#print X_norm


Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])



A = np.sum(Z, axis=1) > 10
#print np.nonzero(A)

A = np.eye(3)
B = np.eye(3)
C = np.vstack((A, B))
print C