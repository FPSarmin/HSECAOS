import numpy as np


def f(A, B, k):
    temp = np.dot(A, B.T)
    temp = temp[np.ix_(range(min(k, len(temp))), range(min(k, len(temp))))]
    answer = np.diagonal(temp)
    return np.sum(answer)


def prod_and_sq_sum(A):
    diag = A.diagonal()
    diag = diag * diag.reshape((1, len(diag)))
    suma = np.sum(diag)
    prod = np.prod(diag)
    return prod, suma


def get_diag(A, B):
    n = len(A)
    A = A.reshape((1, n * n))
    B = B.T.reshape((1, n * n))
    answer = A * B
    answer = np.sum(answer.reshape(n, n))
    return answer


X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(get_diag(X, X1))
# print(np.dot(X, X1.T))
# print(f(X, X1, 4))


