import numpy as np

def matmul(A, B):
    return np.matmul(A, B)


C = np.eye(3)
D = np.array([[1, 2, 3], [4,5,6], [7,8,9]])
C = matmul(C, D)
print(C)