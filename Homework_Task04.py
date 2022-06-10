# 4. Задана натуральная степень n.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени пример записи в файл
# при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0

import random

n = random.randint(1, 10)


def generate_polynom(polynoms, filename):
    result = ""
    for i in range(0, polynoms + 1):
        mult = random.randint(1, 100)
        if mult == 1:
            mult = ''
        result += str(mult) + 'x^' + str(polynoms-i) + ' + '
    result = result[:-5]
    result += ' = 0'
    f = open(filename, 'w')
    f.write(result)
    f.close()
    return result


for i in range(1, 3):
    n = random.randint(1, 10)
    print(generate_polynom(n, 'task04_0' + str(i)))
