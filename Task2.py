import math


def function(x):
    return math.exp(x) - x
    # return math.pow(x, 3) + math.pow(x, 2) * 4 + 3

def separation(m, a, b):
    dic = {}
    for i in range(m + 1):
        dic[a + i * (b - a) / m] = function(a + i * (b - a) / m)
    return dic


def print_table(dic):
    print("%-9s%-9s" % ("x", "f(x)"))
    print("%-9s%-9s" % ("--------", "--------"))
    for key, value in dic.items():
        print("%-9f%-9f" % (key, value))
    print()

def algebraic_interpolation(a, b):
    print("Задача алгебраического интерполирования.\n")
    print("Вариант: 3. Уравнение: f(x)=exp(x) – x, Отрезок: [0, 1]")
    m = int(input("Введите число узлов равзбиения отрезка:")) - 1
    print()
    print("Исходная таблица значений функции:")
    dic = separation(m, a, b)
    print_table(dic)
    go = True
    while go:
        x = float(input("Введите точку интерполирования: "))
        n = int(input(f"Введите степень многочлена меньше {m + 1}: "))
        while n >= m + 1:
            # print()
            n = int(input(f"Введено неверное значение степени, введите степень меньше {m + 1}: "))
        print()
        print("Отсортированная таблица значений функции:")
        dic_new = sort_dic(dic, x, n)
        print_table(dic_new)
        # a = coef(dic_new)
        newton = Newton(dic_new, x, n)
        lagranz = Lagranz(dic_new, x)
        print(f"Значение в x = {x} многочлена Ньютона: {newton}")
        print(f"Значение абсолютной фактической погрешности для многочлена формы Ньютона {abs(function(x) - newton)}")
        print(f"Значение в x = {x} многочлена Лагранжа: {Lagranz(dic_new, x)}")
        print(f"Значение абсолютной фактической погрешности для многочлена формы Лагранжа {abs(function(x) - lagranz)}\n")

        repeat = str(input("Хотите продолжить программу? (Да/Нет)"))
        repeat = repeat.lower()
        if repeat == "да":
            print()
        else:
            go = False

def sort_dic(dic, x, n):
    dic_keys = list(dic.keys())
    dic_values = list(dic.values())
    for i in range(len(dic) - 1):
        for j in range(len(dic) - i - 1):
            if abs(dic_keys[j] - x) > abs(dic_keys[j + 1] - x):
                dic_keys[j], dic_keys[j + 1] = dic_keys[j + 1], dic_keys[j]
                dic_values[j], dic_values[j + 1] = dic_values[j + 1], dic_values[j]
    new_dic = {}
    for j in range(n + 1):
        new_dic[dic_keys[j]] = dic_values[j]
    return new_dic

def Newton(dic, x, n):
    class divided_differences:
        def __init__(self, start, end, value):
            self.start = start
            self.end = end
            self.value = value

    dic_keys = sorted(list(dic.keys()))
    dic_values = []
    for i in range(len(dic_keys)):
        dic_values.append(divided_differences(i, i, dic[dic_keys[i]]))

    coef = []
    # coef.append(dic_values[0])
    coef.append(divided_differences(dic_values[0].start, dic_values[0].end, dic_values[0].value))

    for j in range(1, n + 1):
        for i in range(len(dic_values) - 1):
            dic_values[i].value = (dic_values[i + 1].value - dic_values[i].value) / (dic_keys[dic_values[i + 1].end] - dic_keys[dic_values[i].start])
            dic_values[i].start = dic_values[i].start
            dic_values[i].end = dic_values[i + 1].end
        coef.append(divided_differences(dic_values[0].start, dic_values[0].end, dic_values[0].value))
        dic_values = dic_values[:-1]

    P = coef[0].value
    multiplication = 1
    for i in range(n):
        multiplication *= x - dic_keys[i] # coef[i].start
        P = P + coef[i + 1].value * multiplication
    return P

def Lagranz(dic, x):
    dic_keys = list(dic.keys())
    dic_values = list(dic.values())
    z = 0
    for j in range(len(dic_values)):
        p1 = 1
        p2 = 1
        for i in range(len(dic_keys)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (x - dic_keys[i])
                p2 = p2 * (dic_keys[j] - dic_keys[i])
        z = z + dic_values[j] * p1 / p2

    return z


algebraic_interpolation(0, 1)
