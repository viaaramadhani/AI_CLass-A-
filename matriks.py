#Matriks 
#Octavia Ramadhani_F55123015

import numpy as np

np.random.seed(2)


matrix_2x3 = np.random.randint(1, 10, size=(2, 3))
matrix_3x4 = np.random.randint(1, 10, size=(3, 4))

print("Matrix 2x3:")
print(matrix_2x3)
print("\nMatrix 3x4:")
print(matrix_3x4)

#Ini menggunakan lib numpy matmul
result_with_matmul = np.matmul(matrix_2x3, matrix_3x4)
print("\nHasil dengan menggunakan library:")
print(result_with_matmul)

# Ini tanpa menggunakan lib numpy
def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

hasil_tanpa_library = matrix_multiply(matrix_2x3.tolist(), matrix_3x4.tolist())
print("\nHasil tanpa library:")
print(hasil_tanpa_library)