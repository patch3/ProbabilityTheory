import math
import InComComb
import integrated


def Bernoulli(k, n, p):
    g = 1 - p
    P = InComComb.Combination(n, k) * p ** k * g ** (n - k)
    return P


def LocalLasplaces(k, n, p):
    g = 1.0 - p
    P = (1.0 / math.sqrt(n * p * g)) * (Fe(X(k, n, p)))
    return P


def IntegratedLasplaces(k1, k2, n, p):
    x1 = X(k1, n, p)
    x2 = X(k2, n, p)
    P = (1 / math.sqrt(2.0 * math.pi)) * integrated.TrapezoidRuleInteg(IngEDz, x1, x2, 1000000)
    return P


def IngEDz(z):
    return math.e ** (-z * z / 2.0)


def Fe(x):
    fe = (1.0 / math.sqrt(2.0 * math.pi)) * (math.e ** (-(x * x) / 2.0))
    return fe


def X(k, n, p):
    g = 1 - p
    x = (k - n * p) / math.sqrt(n * p * g)
    return x

