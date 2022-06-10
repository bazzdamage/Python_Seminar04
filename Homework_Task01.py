# 1. Вычислить число Pi по ряду Маджавы
import math


def calc_pi_madhava(iteration, precision):
    n = iteration
    r = precision
    z = 1
    pi = 1
    k = math.sqrt(12)
    for i in range(1, n + 1):
        pi = pi - z / ((2 * i + 1) * math.pow(3, i))
        z *= -1
    pi *= k
    return round(pi, r)


print(calc_pi_madhava(20, 10))
