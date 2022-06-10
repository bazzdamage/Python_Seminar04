# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. (нужно два полинома сложить.
# Файлы взять благодаря предыдущему заданию)

f = open('task04_01', 'r')
polynom_1 = f.readline()
f = open('task04_02', 'r')
polynom_2 = f.readline()


def polynom_to_dict(polynom):
    result = polynom.split(' + ')
    result[-1] = result[-1][:-4]
    res_dict = {}
    for i in result:
        index = i.index('x')
        if len(i[index + 2:]) == 0:
            res_dict[0] = int(i[:index])
        else:
            res_dict[int(i[index + 2:])] = int(i[:index])
    return res_dict


def polynoms_dict_add(pol_1: dict, pol_2: dict):
    if len(pol_1) < len(pol_2):
        pol_1, pol_2 = pol_2, pol_1
    for key in pol_1.keys():
        if key in pol_2.keys():
            pol_1[key] += pol_2[key]
    return pol_1


def dict_to_polynom(pol: dict):
    res = ""
    for key in pol:
        res += str(pol[key]) + "x^" + str(key) + " + "
    res = res[:-5]
    res += ' = 0'
    return res


a = polynom_to_dict(polynom_1)
b = polynom_to_dict(polynom_2)
add = polynoms_dict_add(a, b)
res = dict_to_polynom(add)
print(f'{polynom_1}\n + \n{polynom_2}\n = \n{res}')
