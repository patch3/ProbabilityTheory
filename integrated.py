import math

# number of segments
STD_NUMBER_SEGMENTS = 100

"""Правило трапеций
    nseg - число отрезков, на которые разбивается [a;b]"""


def TrapezoidRuleInteg(func, a, b, nseg=STD_NUMBER_SEGMENTS):
    dx = 1.0 * (b - a) / nseg
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        sum += func(a + i * dx)
    return sum * dx
