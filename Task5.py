import math


def function(x):
    return 4
    # return 4 * math.pow(x, 3) + 1
    # return 3 * math.pow(x, 5)
    # return math.sqrt(1 - 1/2 * math.pow(math.sin(x), 2))

def antiderivative(x):
    return 4 * x
    # return math.pow(x, 4) + x
    # return 1 / 2 * math.pow(x, 6)
    # return 1.3506438810476755025201747353387258413495223669243  # 49 знаков после запятой

def p(x):
    return 1


# def Legendre(x, N):
#     P0 = 1
#     P1 = x
#     for i in range(2, N + 1):
#         P2 = (2 * N - 1) / N * P1 * x - (N - 1) / N * P0
#         P0 = P1
#         P1 = P2
#
#     return P1

def Legendre(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2 * n - 1) / n * Legendre(x, n - 1) * x - (n - 1) / n * Legendre(x, n - 2)

def separating_roots_equation(A, B, function, N = 10000):
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

def Gauss(N, function, Legendre, a, b):

    def new_funciton(x):
        return Legendre(x, N)

    mas = separating_roots_equation(-1, 1, new_funciton)
    mast = []
    masc = []
    e = math.pow(10, -12)
    for i in range(len(mas)):
        mast.append(half_division(mas[i][0], mas[i][1], e, new_funciton))
        masc.append((2 * (1 - math.pow(mast[i], 2))) / (math.pow(N, 2) * math.pow(Legendre(mast[i], N - 1), 2)))

    P = 0
    for i in range(N):
        P += masc[i] * function((b - a) / 2 * mast[i] + (b + a) / 2)

    return (b - a) / 2 * P

def first():
    print("Задача приближённого вычисления интеграла по составной КФ Гаусса.\n")

    for N in range(1, 9):
        def new_funciton(x):
            return Legendre(x, N)

        mas = separating_roots_equation(-1, 1, new_funciton)
        mast = []
        masc = []
        e = math.pow(10, -12)
        for i in range(len(mas)):
            mast.append(half_division(mas[i][0], mas[i][1], e, new_funciton))
            masc.append((2 * (1 - math.pow(mast[i], 2))) / (math.pow(N, 2) * math.pow(Legendre(mast[i], N - 1), 2)))

        print("Для N = ", N, ":")
        print("Узлы многочлена Лежандра:        ", mast)
        print("Соответствующии им коэффициенты: ", masc, "\n")

def second():
    print("Задача приближённого вычисления интеграла по составной КФ Гаусса.\n")
    a = int(input("Введите левый край отрезка [a, b]: "))
    b = int(input("Введите правый край отрезка [a, b]: "))
    N = int(input("Введите число отрезков разбиения отрезка: "))

    J = antiderivative(b) - antiderivative(a)
    # J = antiderivative(1)
    print(f"\nОпределенный интегралл на промежутке [{a}, {b}] J: ", J, "\n")

    print("Квадратурная формула Гаусса:")
    J_h = Gauss(N, function, Legendre, a, b)
    print("Приближенное значение J(h): ", J_h)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))

def third():
    print("Задача приближённого вычисления интеграла по составной КФ Гаусса.\n")
    # a = int(input("Введите левый край отрезка [a, b]: "))
    # b = int(input("Введите правый край отрезка [a, b]: \n"))
    a = 0
    b = math.pi / 2

    masN = [4, 5 ,6, 8, 12]

    for N in masN:
        def new_funciton(x):
            return Legendre(x, N)

        mas = separating_roots_equation(-1, 1, new_funciton)
        mast = []
        masc = []
        mastNew = []
        mascNew = []
        e = math.pow(10, -12)
        for i in range(len(mas)):
            mast.append(half_division(mas[i][0], mas[i][1], e, new_funciton))
            masc.append((2 * (1 - math.pow(mast[i], 2))) / (math.pow(N, 2) * math.pow(Legendre(mast[i], N - 1), 2)))

        P = 0
        for i in range(N):
            mastNew.append((b - a) / 2 * mast[i] + (b + a) / 2)
            mascNew.append(masc[i] * (b - a) / 2)
            P += mascNew[i] * function(mastNew[i])

        print(f"Квадратурная формула Гаусса для N = {N} и отрезка [{a}, {b}]:")
        J_h = Gauss(N, function, Legendre, a, b)
        print("Узлы многочлена Лежандра:        ", mastNew)
        print("Соответствующии им коэффициенты: ", mascNew)
        print("Приближенное значение J(h): ", J_h, "\n")

    repeat = str(input("Хотите продолжить программу? (Да/Нет) "))
    repeat = repeat.lower()
    if repeat == "да":
        repeat = True
        print()
    else:
        repeat = False

    while repeat:
        a = int(input("Введите левый край отрезка [a, b]: "))
        b = int(input("Введите правый край отрезка [a, b]: "))

        masN = [4, 5, 6, 8, 12]

        for N in masN:
            def new_funciton(x):
                return Legendre(x, N)

            mas = separating_roots_equation(-1, 1, new_funciton)
            mast = []
            masc = []
            mastNew = []
            mascNew = []
            e = math.pow(10, -12)
            for i in range(len(mas)):
                mast.append(half_division(mas[i][0], mas[i][1], e, new_funciton))
                masc.append(
                    (2 * (1 - math.pow(mast[i], 2))) / (math.pow(N, 2) * math.pow(Legendre(mast[i], N - 1), 2)))

            P = 0
            for i in range(N):
                mastNew.append((b - a) / 2 * mast[i] + (b + a) / 2)
                mascNew.append(masc[i] * (b - a) / 2)
                P += mascNew[i] * function(mastNew[i])

            print(f"Квадратурная формула Гаусса для N = {N} и отрезка [{a}, {b}]:")
            J_h = Gauss(N, function, Legendre, a, b)
            print("Узлы многочлена Лежандра:        ", mastNew)
            print("Соответствующии им коэффициенты: ", mascNew)
            print("Приближенное значение J(h): ", J_h, "\n")

        repeat = str(input("Хотите продолжить программу? (Да/Нет) "))
        repeat = repeat.lower()
        if repeat == "да":
            repeat = True
            print()
        else:
            repeat = False

# first()
second()
# third()