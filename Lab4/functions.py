import math

import numpy as np


def count_condition_number(A):
    inv = np.linalg.inv(A)
    return np.linalg.norm(A) * np.linalg.norm(inv)


def find_max(A):
    n = len(A)
    k, l = 0, 0
    max = A[0, 1]
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i, j]) > abs(max):
                max = abs(A[i, j])
                k = i
                l = j
    return k, l


def count_norm(A):
    n = len(A)
    sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum += A[i, j] ** 2
    return math.sqrt(sum)


def count_rotation(A, k, l):
    if A[k, k] == A[l, l]:
        return math.pi / 4
    return math.atan(2 * A[k, l] / (A[k, k] - A[l, l])) / 2


def jacobi(A, eps):
    iterations = 0
    n = len(A)
    vec = np.eye(n, n)
    while count_norm(A) > eps:
        iterations += 1
        k, l = find_max(A)
        deg = count_rotation(A, k, l)
        rotation = np.eye(n, n)

        cos = math.cos(deg)
        sin = math.sin(deg)

        rotation[k, k], rotation[l, l] = cos, cos
        rotation[k, l], rotation[l, k] = -sin, sin

        rotation_transpose = rotation.transpose()

        A = np.dot(np.dot(rotation_transpose, A), rotation)
        vec = np.dot(vec, rotation)

    return np.diag(A), vec, iterations






