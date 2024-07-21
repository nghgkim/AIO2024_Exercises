import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)

    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = result = np.dot(vector1, vector2)

    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)

    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)

    return result


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print(round(result, 2))

v1 = np. array([0, 1, -1, 2])
v2 = np. array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))

x = np. array([[1, 2],
               [3, 4]])
k = np. array([1, 2])
print('result \n', x.dot(k))

x = np. array([[-1, 2],
               [3, -4]])
k = np. array([1, 2])
print('result \n', x @ k)

m = np. array([[-1, 1, 1], [0, -4, 9]])
v = np. array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)

m1 = np. array([[0, 1, 2], [2, -3, 1]])
m2 = np. array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

m1 = np.eye(3)
m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print(result)

m1 = np.eye(2)
m1 = np. reshape(m1, (-1, 4))[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

m1 = np. array([[1, 2], [3, 4]])
m1 = np. reshape(m1, (-1, 4), "F")[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)
