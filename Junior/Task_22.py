import math

from cmath import sqrt
from random import randint


def distance_2D(a, b):
    l_0 = abs(a[0] - b[0])
    l_1 = abs(a[1] - b[1])
    DistanceBetweenPoints_2D = sqrt((l_0**2) + (l_1**2))
    return DistanceBetweenPoints_2D


def distance_3D(a, b):
    la = abs(A[0] - B[0])
    lb = abs(A[1] - B[1])
    lc = abs(A[2] - B[2])
    DistanceBetweenPoints_3D = sqrt((la**2) + (lb**2) + (lc**2))
    return DistanceBetweenPoints_3D


def fill_list(list):
    i = 0
    while(i < 3):
        n = randint(-3, 3)
        list.append(n)
        i += 1
    return list


A = []
B = []

fill_list(A)
print(A)

fill_list(B)
print(B)

print(f'{distance_2D(A, B): .3f}')
print(f'{distance_3D(A, B): .3f}')
