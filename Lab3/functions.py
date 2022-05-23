import random
import time

import numpy as np
import scipy.sparse as scs



def lil_row_product(matrix1, matrix2, row_idx1, row_idx2):
    row1 = matrix1.rows[row_idx1]
    row2 = matrix2.rows[row_idx2]
    data1 = matrix1.data[row_idx1]
    data2 = matrix2.data[row_idx2]

    res = 0
    i1 = i2 = 0

    while i1 < len(row1) and i2 < len(row2):
        col_idx1 = row1[i1]
        col_idx2 = row2[i2]

        if col_idx1 == col_idx2:
            res += data1[i1] * data2[i2]
            i1 += 1
        elif col_idx1 < col_idx2:
            i1 += 1
        else:
            i2 += 1

    return res


def csr_row_iter(csr, row_idx):
    row_len = csr.shape[1]
    data_start = csr.indptr[row_idx]
    data_end = csr.indptr[row_idx + 1] if row_idx + 1 < csr.shape[0] else len(csr.data)

    j = 0

    for data_idx in range(data_start, data_end):
        col = csr.indices[data_idx]
        val = csr.data[data_idx]

        while j < col:
            yield 0
            j += 1

        yield val
        j += 1

    for _ in range(j, row_len):
        yield 0


def empty_matrix(n, m, format):
    Matrix = scs.__dict__[format + "_matrix"]
    return Matrix((n, m))


def identity_matrix(n, format):
    return scs.identity(n, format=format)


def lu_decomposition(A):
    N = A.shape[0]
    L = identity_matrix(N, "lil")
    U = empty_matrix(N, N, "lil")  # транспонированная

    for i in range(N):
        for j, a in zip(range(N), csr_row_iter(A, i)):
            num = a - lil_row_product(U, L, j, i)

            if i <= j:
                U[j, i] = num
            else:
                L[i, j] = num / U[j, j]

    return L.tocsr(), U.transpose().tocsr()


def lower_trivial_system_solution(A, b):
    x = np.zeros(len(b))
    x[0] = b[0]

    for i in range(1, len(b)):
        x[i] = b[i] - A[i] * x

    return x


def upper_trivial_system_solution(A, b):
    N = len(b)
    x = np.zeros(N)
    x[-1] = b[-1] / A[-1, -1]

    for i in reversed(range(N - 1)):
        x[i] = (b[i] - A[i] * x) / A[i, i]

    return x


def system_solution(A, b):
    start_time = time.time()
    L, U = lu_decomposition(A)
    y = lower_trivial_system_solution(L, b)
    x = upper_trivial_system_solution(U, y)
    end_time = time.time()
    return x, end_time - start_time


'''def LU(A):
    n = A.indptr.size - 1
    L = csr_matrix(([], [], [0] * (n + 1)), shape=(n, n), dtype=np.float64)
    U = csr_matrix(([], [], [0] * (n + 1)), shape=(n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            U[0, i] = A[0, i]
            L[i, 0] = A[i, 0] / U[0, 0]
            s = 0.0
            for k in range(i):
                s += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - s

            if i > j:
                L[j, i] = 0
            else:
                s = 0.0
                for k in range(i):
                    s += L[j, k] * U[k, i]
                L[j, i] = (A[j, i] - s) / U[i, i]
    return L, U


def forward_sub(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        tmp = b[i]
        for j in range(i-1):
            tmp -= L[i,j] * x[j]
        x[i] = tmp / L[i,i]
    return x


def back_sub(U, b):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        tmp = b[i]
        for j in range(i+1, n):
            tmp -= U[i,j] * x[j]
        x[i] = tmp / U[i,i]
    return x


def solve_lu1(A, b):
    start_time = time.time()
    L, U = LU(A)
    y = forward_sub(L, b)
    x = back_sub(U, y)
    end_time = time.time()
    return x, end_time - start_time


def solve_lu2(A, b):
    start_time = time.time()
    L, U = LU(A)
    n = len(U.indptr) - 1

    y = np.array([])

    iter_ = 0

    for i in range(0, n):
        s = 0
        for k in range(0, i):
            s += y[k] * L[i, k]
        y = np.append(y, b[i] - s)
        iter_ += 1

    x = np.zeros(n)

    for i in range(0, n):
        s = 0

        for k in range(0, i):
            s += U[n - i - 1, n - k - 1] * x[n - k - 1]

        x[n - i - 1] = 1/U[n - i - 1, n - i - 1] * (y[n - i - 1] - s)
        iter_ += 1
    end_time = time.time()
    return x, end_time - start_time


def solve_lu3(A, b):
    start_time = time.time()
    L, U = LU(A)
    L_inv = np.linalg.inv(L.toarray())
    U_inv = np.linalg.inv(U.toarray())
    tmp = U_inv @ (L_inv @ b)
    end_time = time.time()
    return tmp, end_time - start_time'''


def seidel_row_vec_product(csr, vec1, vec2, row_idx):
    start_idx = csr.indptr[row_idx]
    end_idx = csr.indptr[row_idx + 1] if row_idx + 1 < csr.shape[0] else len(csr.data)

    curr_vec = vec1
    product = 0
    diag_value = 0

    for i in range(start_idx, end_idx):
        col_idx = csr.indices[i]
        val = csr.data[i]

        if col_idx >= row_idx:
            curr_vec = vec2

        if col_idx == row_idx:
            diag_value = val
            continue

        product += val * curr_vec[col_idx]

    return product, diag_value


def seidel_method(A, b, eps=1e-6, max_iter=250):
    start_time = time.time()
    n = A.shape[0]
    x = np.array(b)

    for _ in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            product, diag_value = seidel_row_vec_product(A, x_new, x, i)
            x_new[i] = (b[i] - product) / diag_value

        if np.allclose(x, x_new, rtol=eps):
            break

        x = x_new
    end_time = time.time()
    return x, end_time - start_time


def get_e_matrix(n):
    e_matrix = scs.csr_matrix(([], [], [0] * (n + 1)), shape=(n, n), dtype=np.float64)
    e_matrix.setdiag(1)
    return e_matrix


def inverse_matrix(L, U):
    n = len(L.indptr) - 1
    e_matrix = get_e_matrix(n)
    y = np.array([])
    result_matrix = [np.array([])]
    for k in range(0, n):
        e = e_matrix.getrow(k).toarray()[0]
        temp = np.array([])
        for i in range(0, n):
            sum = 0
            for p in range(0, i):
                sum += L[i, p] * temp[p]
            yi = e[i] - sum
            temp = np.append(temp, yi)
        y = np.append(y, temp)

    y = y.reshape(n, n)

    for k in range(0, n):
        yi = y[k]
        x = np.zeros(n)
        for i in range(0, n):
            sum = 0
            for k in range(0, i):
                sum += U[n - i - 1, n - k - 1] * x[n - k - 1]
            x[n - i - 1] = 1 / U[n - i - 1, n - i - 1] * (yi[n - i - 1] - sum)
        result_matrix = np.append(result_matrix, x)
    return result_matrix.reshape(n, n).transpose()


def generate_gilbert(k):
    A = scs.csr_matrix(([], [], [0] * (k + 1)), shape=(k, k), dtype=np.float64)
    for i in range(k):
        for j in range(k):
            A[i, j] = 1 / (i + j + 1)
    return A


def generate_diagonal_dominance_matrix(k):
    A_k = scs.csr_matrix(([], [], [0] * (k + 1)), shape=(k, k), dtype=np.float64)

    for i in range(k):
        for j in range(k):
            if i != j:
                A_k[i, j] = -1
            else:
                A_k[i, j] = k + 1
    return A_k


def generate_random_matrix(k):
    A = scs.csr_matrix(([], [], [0] * (k + 1)), shape=(k, k), dtype=np.float64)
    for i in range(k):
        for j in range(k):
            A[i, j] = random.randint(-10, 10)
    return A


def generate_vector(A):
    n = A.indptr.size
    x = []
    for i in range(1, n):
        x.append(i)
    return np.dot(A.toarray(), x)