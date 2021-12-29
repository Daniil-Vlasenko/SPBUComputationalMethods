import math

def f(x):
    # return math.sin(x)
    return math.exp(2 * x)

def q(x):
    return 1/math.pow(x, 1/2)

def function(x, f, q):
    return f(x) * q(x)

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

def mastMasc(N, Legendre):
    def new_funciton(x):
        return Legendre(x, N)

    mas = separating_roots_equation(-1, 1, new_funciton)
    mast = []
    masc = []
    e = math.pow(10, -12)
    for i in range(len(mas)):
        mast.append(half_division(mas[i][0], mas[i][1], e, new_funciton))
        masc.append((2 * (1 - math.pow(mast[i], 2))) / (math.pow(N, 2) * math.pow(Legendre(mast[i], N - 1), 2)))

    return [mast, masc]

def Gauss(N, function, a, b, mast, masc):
    def new_function(x):
        return function(x, f, q)

    P = 0
    for i in range(N):
        P += masc[i] * new_function((b - a) / 2 * mast[i] + (b + a) / 2)

    return (b - a) / 2 * P

def compositeGaussQF():
    a = int(input('Введите левый край отрезка интегрирования, a: '))
    b = int(input('Введите правый край отрезка интегрирования, b: '))
    m = int(input('Введите число промежутков деления, m: '))
    N = int(input('Введите число узлов КФ Гаусса, N: '))

    mas = mastMasc(N, Legendre)
    print(f'\nУзлы многочлена Лежандра для N = {N}: \n{mas[0]}')
    print(f'Коэффициенты соответствующие узлам многочлена Лежандра для N = {N}: \n{mas[1]}')

    compositeP = 0
    for i in range(m):
        a_new = a + i * (b - a) / m
        b_new = a + (i + 1) * (b - a) / m
        compositeP += Gauss(N, function, a_new, b_new, mas[0], mas[1])

    print(f'Значение интеграла полученное через составную КФ Гаусса: {compositeP}\n')

    return compositeP

# для p = 1 / sqrt(x)
def momentsWeightFunction(a, b):
    moments = []
    for k in range(4):
        moments.append((math.pow(b, k + 1 / 2) - math.pow(a, k + 1 / 2)) / (k + 1 / 2))
    return moments

def GaussTypeFunction():
    a = int(input('Введите левый край отрезка интегрирования, a: '))
    b = int(input('Введите правый край отрезка интегрирования, b: '))

    moments = momentsWeightFunction(a, b)

    a1 = (moments[0] * moments[3] - moments[2] * moments[1]) / (moments[1] * moments[1] - moments[2] * moments[0])
    a2 = (moments[2] * moments[2] - moments[3] * moments[1]) / (moments[1] * moments[1] - moments[2] * moments[0])

    masx =[]

    masx.append(((-1) * a1 + (a1 ** 2 - 4 * a2) ** (1 / 2)) / 2)
    masx.append(((-1) * a1 - (a1 ** 2 - 4 * a2) ** (1 / 2)) / 2)

    A1 = (moments[1] - masx[1] * moments[0]) / (masx[0] - masx[1])
    A2 = (moments[1] - masx[0] * moments[0]) / (masx[1] - masx[0])

    P = A1 * f(masx[0]) + A2 * f(masx[1])

    def check(x):
        return math.pow(x, 3)

    PCheck = A1 * check(masx[0]) + A2 * check(masx[1])
    PCheckReal = 2 / 7 * (math.pow(b, 7 / 2) - math.pow(a, 7 / 2))
    print(f'\nЗначения моментов весовой функции: {moments[0]}, {moments[1]}, {moments[2]}, {moments[3]}')
    print(f'Получаем уравнение: x^2 + {a1}x + {a2} = 0')
    print(f'Корни: x1 = {masx[0]} и x2 = {masx[1]}')
    print(f'Коэффициенты КФ: A1 = {A1} и A2 = {A2}')
    print(f'Значение интеграла полученное через КФ типа Гаусса: {P}')
    print(f'        Проверка. Значение интеграла полученное через КФ типа Гаусса для x^3: {PCheck}')
    print(f'        Абсолютная погрешность: {math.fabs(PCheckReal - PCheck)}')

    return P

def Meler():
    N1 = int(input('Введите число узлов, N1: '))
    N2 = int(input('Введите число узлов, N2: '))
    N3 = int(input('Введите число узлов, N3: '))
    masN1 = []
    masN2 = []
    masN3 = []
    P1, P2, P3 = 0, 0, 0

    for k in range(1, N1 + 1):
        masN1.append(math.cos((2 * k - 1) / (2 * N1) * math.pi))
        P1 += math.pi / N1 * f(masN1[k - 1])
    for k in range(1, N2 + 1):
        masN2.append(math.cos((2 * k - 1) / (2 * N2) * math.pi))
        P2 += math.pi / N2 * f(masN2[k - 1])
    for k in range(1, N3 + 1):
        masN3.append(math.cos((2 * k - 1) / (2 * N3) * math.pi))
        P3 += math.pi / N3 * f(masN3[k - 1])

    print(f'\nКоэффициенты для N1: {math.pi / N1}')
    print(f'Корни для N1: {masN1}')
    print(f'Приближенное значение интегралла для N1: {P1}\n')
    print(f'Коэффициенты для N2: {math.pi / N2}')
    print(f'Корни для N2: {masN2}')
    print(f'Приближенное значение интегралла для N2: {P2}\n')
    print(f'Коэффициенты для N3: {math.pi / N3}')
    print(f'Корни для N3: {masN3}')
    print(f'Приближенное значение интегралла для N3: {P3}')


print('Задача приближённого вычисления интегралов при помощи квадратурных формул Наивысшей Алгебраической Степени Точности\n')
isTrue = True
while isTrue:
    # compositeGaussQF()
    # GaussTypeFunction()
    Meler()

    isTrue = str(input("\nХотите продолжить программу? (Да/Нет) "))
    isTrue = isTrue.lower()
    if isTrue == "да":
        isTrue = True
        print()
    else:
        isTrue = False