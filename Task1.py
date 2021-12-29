"""Требуется найти все корни уравнения (1) на [A, B] нечетной кратности (здесь A, B, f(x) –
параметры задачи).
Решение задачи разбить на два этапа:
1. Процедура отделения корней уравнения (1) на отрезке [A, B];
2. Уточнение корней уравнения (1) на отрезках перемены знака вида [ai, bi]
    a. Методом половинного деления (методом бисекции);
    b. Методом Ньютона (методом касательных);
    c. Модифицированным методом Ньютона;
    d. Методом секущих

f(x)= 2^x ‒ 2 cos(x) [A, B] = [-8; 10] ε = 10^-6            (1)
"""
import math

task = "ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ\nf(x)= 2^x ‒ 2 cos(x)      [A, B] = [-8; 10]       ε = 10^-6\n"
def print_task(task):
    print(task)

def function(x):
    return math.pow(2, x) - 2 * math.cos(x)

def dfunction(x):
    return math.log(2, math.exp(1)) * math.pow(2, x) + 2 * math.sin(x)

A = -8
B = 10
e = math.pow(10, -10)

def separating_roots_equation(A, B, function, N = 100):
    H = (B - A)/N
    Counter = 0
    X1 = A
    X2 = X1 + H
    Y1 = function(X1)
    mas = []

    while X2 <= B:
        Y2 = function(X2)

        if Y1 * Y2 <= 0:
            Counter += 1
            mas.append([X1, X2])
            print(f"[{X1}, {X2}]")

        X1 = X2
        X2 = X1 + H
        Y1 = Y2

    print(f"Число отрезков: {Counter}\n\n\n")
    return mas

def half_division(a, b, e, function):
    print("Метод половинного деления (методом бисекции)\n")
    print(f"Начальное приближение к корню: {(b + a) / 2}")
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
    print(f"Количество шагов: {Counter}")
    print(f"Приближенное решение уравнения: {X}")
    print(f"|x(m) - x(m+1)|: {(b - a) / 2}")
    print(f"Абсолютная величина невязки: {function(X) - 0}\n\n")
    return X

def newton(a, b, e, function):
    print("Метод Нютона\n")
    Counter = 0
    try:
        print(f"Начальное приближение к корню: {(b + a) / 2}")
        c = (a + b) / 2
        x = c - function(c) / dfunction(c)
        while abs(x - c) > e:
            Counter += 1
            c = x
            x = c - function(c) / dfunction(c)

        print(f"Количество шагов: {Counter}")
        print(f"Приближенное решение уравнения: {x}")
        print(f"|x(m) - x(m+1)|: {(x - c) / 2}")
        print(f"Абсолютная величина невязки: {function(x) - 0}\n\n")
        return x

    except:
        print(f"Данный метод не подходит выбранной функции на отрезке [{a}, {b}]")

def modnewton(a, b, e, function):
    print("Модифицированный метод Нютона\n")
    Counter = 0
    try:
        print(f"Начальное приближение к корню: {(b + a) / 2}")
        c0 = (a + b) / 2
        c = c0
        x = c - function(c) / dfunction(c0)
        while abs(x - c) > e:
            Counter += 1
            c = x
            x = c - function(c) / dfunction(c0)

        print(f"Количество шагов: {Counter}")
        print(f"Приближенное решение уравнения: {x}")
        print(f"|x(m) - x(m+1)|: {(x - c) / 2}")
        print(f"Абсолютная величина невязки: {function(x) - 0}\n\n")
        return x

    except:
        print(f"Данный метод не подходит выбранной функции на отрезке [{a}, {b}]")

def secant (a, b, e, function):
    print("Метод секущих\n")
    Counter = 0
    try:
        print(f"Начальное приближение к корню: {(b + a) / 2}")
        predpredx = (a + b) / 2
        predx = predpredx - function(predpredx) / dfunction(predpredx)
        x = predx - (function(predx) / (function(predx) - function(predpredx))) * (predx - predpredx)
        while abs(x - predx) > e:
            Counter += 1
            predpredx = predx
            predx = x
            x = predx - (function(predx) / (function(predx) - function(predpredx))) * (predx - predpredx)

        print(f"Количество шагов: {Counter}")
        print(f"Приближенное решение уравнения: {x}")
        print(f"|x(m) - x(m+1)|: {(x - predx) / 2}")
        print(f"Абсолютная величина невязки: {function(x) - 0}\n\n")
        return x

    except:
        print(f"Данный метод не подходит выбранной функции на отрезке [{a}, {b}]")




print_task(task)
mas = separating_roots_equation(A, B, function)

for i in mas:
    print(f"Отрезок {i}:\n")
    half_division(i[0], i[1], e, function)
    newton(i[0], i[1], e, function)
    modnewton(i[0], i[1], e, function)
    secant(i[0], i[1], e, function)
