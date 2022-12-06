import math


def Combination(n, m):
    C = math.factorial(n) / \
        (math.factorial(m) * math.factorial(n-m))
    return C
