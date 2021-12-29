import math


def function(x):
    return math.exp(x) - x

def separation(m, a, b):
    dic = {}
    for i in range(m + 1):
        dic[a + i * (b - a) / m] = function(a + i * (b - a) / m)
    return dic

def replacement(dic):
    new_dic = {}
    for key, value in dic.items():
        new_dic[value] = key
    return new_dic

def print_table1(dic):
    print("%-30s%-30s" % ("f(x)", "x"))
    print("%-30s%-30s" % ("--------", "--------"))
    for key, value in dic.items():
        print("%-30s%-30s" % (key, value))
    print()

def print_table2(dic):
    print("%-30s%-30s" % ("x", "f(x)"))
    print("%-30s%-30s" % ("--------", "--------"))
    for key, value in dic.items():
        print("%-30s%-30s" % (key, value))
    print()

def sort_dic1(dic, x, n):
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

def sort_dic2(dic, F, n):
    dic_keys = list(dic.keys())
    dic_values = list(dic.values())
    for i in range(len(dic) - 1):
        for j in range(len(dic) - i - 1):
            if abs(dic_values[j] - F) > abs(dic_values[j + 1] - F):
                dic_keys[j], dic_keys[j + 1] = dic_keys[j + 1], dic_keys[j]
                dic_values[j], dic_values[j + 1] = dic_values[j + 1], dic_values[j]
    new_dic = {}
    for j in range(n + 1):
        new_dic[dic_keys[j]] = dic_values[j]
    return new_dic

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

def separating_roots_equation(a, b, function, N = 1000):
    H = (b - a) / N
    Counter = 0
    X1 = a
    X2 = X1 + H
    Y1 = function(X1)
    mas = []

    while X2 <= b:
        Y2 = function(X2)
        if Y1 * Y2 <= 0:
            Counter += 1
            mas.append([X1, X2])
            print(f"[{X1}, {X2}]")
        X1 = X2
        X2 = X1 + H
        Y1 = Y2

    return mas

def half_division(a, b, e, function):
    Counter = 0
    while True:
        Counter += 1
        c = (a + b) / 2
        if function(a) * function(c) <= 0:
            b = c
        else:
            a = c

        if b - a <= 2 * e:
            break
    X = (b + a) / 2

    return X

def reverseInterpolation1(a, b):
    m = int(input("Введите число узлов разбиения отрезка:")) - 1
    print()
    print("Исходная таблица значений функции:")
    dic = separation(m, a, b)
    dic = replacement(dic)
    print_table1(dic)

    F = float(input("Введите точку обратного интерполирования: "))
    n1 = int(input(f"Введите степень многочлена n1 меньше {m + 1}: "))
    while n1 >= m + 1:
        n1 = int(input(f"Введено неверное значение степени, введите степень n1 меньше {m + 1}: "))
    print()
    print("Отсортированная таблица значений функции:")
    dic_new = sort_dic1(dic, F, n1)
    print_table1(dic_new)
    lagrang = Lagranz(dic_new, F)
    print(f"Значение в F = {F} для первого способа: {lagrang}")
    print(f"Модуль невязки: {abs(function(lagrang) - F)}\n")

def reverseInterpolation2(a, b, e):
    m = int(input("Введите число узлов разбиения отрезка:")) - 1
    print()
    print("Исходная таблица значений функции:")
    dic = separation(m, a, b)
    print_table2(dic)

    F = float(input("Введите точку обратного интерполирования: "))
    n2 = int(input(f"Введите степень многочлена n2 меньше {m + 1}: "))
    while n2 >= m + 1:
        n2 = int(input(f"Введено неверное значение степени, введите степень n2 меньше {m + 1}: "))
    print()
    print("Отсортированная таблица значений функции:")
    dic_new = sort_dic2(dic, F, n2)
    xNear = list(dic_new.keys())[0]
    print_table2(dic_new)

    def new_funciton(xNear):
        return Newton(dic_new, xNear, n2) - F

    mas = separating_roots_equation(a, b,  new_funciton)
    if len(mas) == 0:
        print("Уравнение P(x) - F = 0 не имеет корней на заданном отрезке")
    for i in mas:
        x = half_division(i[0], i[1], e, new_funciton)

        print(f"Значение в F = {F} для второго способа: {x}")
        print(f"Модуль невязки: {abs(function(x) - F)}\n")



def reverseInterpolation():
    print("Задача обратного алгебраического интерполирования.\n")
    print(f"Вариант: 3. Уравнение: f(x)=exp(x) – х ")

    go = True
    while go:
        i = int(input("Какой способ обратного интерполирвания провести? (1/2): "))
        a = int(input("Введите левый край отрезка [a, b]: "))
        b = int(input("Введите правый край отрезка [a, b]: "))

        if i == 1:
            reverseInterpolation1(a, b)
        else:
            # e = math.pow(10, -10)
            e = float(input("Введите точность приближения e: "))
            reverseInterpolation2(a, b, e)

        repeat = str(input("Хотите продолжить программу? (Да/Нет)"))
        repeat = repeat.lower()
        if repeat == "да":
            print()
        else:
            go = False


reverseInterpolation()