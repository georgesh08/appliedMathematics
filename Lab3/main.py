import functions
import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

'''
# Using iterative Seidel method to solve system of linear equations for diagonal dominance matrix
A = functions.generate_diagonal_dominance_matrix(3)
b = [-3, 8, 2]
solution, iter = functions.seidel(A, b, 0.001)
print("Matrix A:\n", A.toarray())
print("Vector b:\n", b)
print("Solution: ", solution, "\nTotal iterations:", iter)'''

'''
# Using LU decomposition to solve system of linear equations
A = [[2, 1, 1], [1, -1, 0], [3, -1, 2]]
A = csr_matrix(A)
b = [2, -2, 2]
solution = functions.solve_system_lu(A, b)
print("Matrix A:\n", A.toarray())
print("Vector b:\n", b)
print("Solution: \n", solution)'''

print("Dominance matrix:")

lu_time = []
seidel_time = []
size = []
for i in range(10, 200, 10):
    A = functions.generate_diagonal_dominance_matrix(i)
    b = functions.generate_vector(A)
    solution1_1, time1 = functions.system_solution(A, b)
    solution1_2, time2 = functions.seidel_method(A, b)
    size.append(i)
    lu_time.append(time1)
    seidel_time.append(time2)
    print("K = ", i, "\nLu time: ", time1, "\nSeidel time: ", time2)

plt.title("Dependency of execution time from matrix size in LU system solution and Seidel iterative method")
plt.xlabel("size")
plt.ylabel("time")
plt.grid()
plt.plot(size, lu_time, size, seidel_time)
plt.show()