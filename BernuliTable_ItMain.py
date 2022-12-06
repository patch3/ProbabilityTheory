import ProbabilityTheory

# не меняй значение пожалуйста
TABLE_LENGTH = 21
HORIZONTAL_LINE = '-' * TABLE_LENGTH


def Main():
    n = int(input("n: "))  # 11
    p = float(input("p: "))  # 0,3
    sum = 0
    print(HORIZONTAL_LINE + "\n|  k  |      P      |\n" + HORIZONTAL_LINE)
    for k in range(n + 1):
        probability = ProbabilityTheory.Bernoulli(k, n, p)
        sum += probability
        print("| {0:3d} | {1:8f}... |".format(k, probability))
    print(HORIZONTAL_LINE + "\n| Sum | {0:11f} |\n".format(sum) + HORIZONTAL_LINE)
    return


Main()
