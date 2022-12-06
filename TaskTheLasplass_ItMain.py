import ProbabilityTheory

# константы по заданию
n = 700
p = 0.35


def Main():
    print("n =", n, ", p =", p, ", g =", 1 - p, ";")
    k  = float(input("k : "))  # 270
    k1 = float(input("k1: "))  # 230
    k2 = float(input("k2: "))  # 270
    k3 = float(input("k3: "))  # 270

    x = ProbabilityTheory.X(k, n, p)
    print("a)\tx   = ", x)
    fe = ProbabilityTheory.Fe(x)
    print("\tfe  = ",  fe)
    P1 = ProbabilityTheory.LocalLasplaces(k, n, p)
    print("\tP   = ", P1, "\n")

    x21 = ProbabilityTheory.X(k1, n, p)
    print("b)\tx1  = ", x21)
    x22 = ProbabilityTheory.X(k2, n, p)
    print("\tx2  = ",   x22)
    P2 = ProbabilityTheory.IntegratedLasplaces(k1, k2, n, p)
    print("\tP2  = ", P2, "\n")

    x31 = ProbabilityTheory.X(k3, n, p)
    print("c)\tx1  = ", x31)
    x32 = ProbabilityTheory.X(n, n, p)
    print("\tx2  = ",   x32)
    P3 = ProbabilityTheory.IntegratedLasplaces(k3, n, n, p)
    print("\tP3  = ", P3, "\n")


Main()
