import math

def function(x):

    # return 4
    # return 4 * x
    # return 4 * math.pow(x, 3)
    # return 6 * math.pow(x, 5)
    return math.exp(x)

def antiderivative(x):

    # return 4 * x
    # return 2 * math.pow(x, 2)
    # return math.pow(x, 4)
    # return math.pow(x, 6)
    return math.exp(x)

class Function1:
    def __init__(self, key, value1, value2):
        self.key = key
        self.value1 = value1
        self.value2 = value2

class Section:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

def separation(m, a, b):
    mas = []
    for i in range(m + 1):
        key = a + i * (b - a) / m
        value1 = function(a + i * (b - a) / m)
        value2 = antiderivative(a + i * (b - a) / m)
        mas.append(Function1(key, value1, value2))

    return mas

def separation2(m, a, b):
    mas = []
    h = (b - a) / m
    for i in range(m + 1):
        af = function(a + i * h)
        bf = function(a + (i + 1) * h)
        wf = function(a + i * h + h / 2)

        mas.append(Section(af, bf, wf))

    return mas

def Lagranz(mas, x):
    dic_keys = []
    dic_values = []
    for i in range(len(mas)):
        dic_keys.append(mas[i].key)
        dic_values.append(mas[i].value1)
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

def leftRectangles(a, b, n, mas, Lagranz):
    # h = (b - a) / n
    # a_new = a
    # P = 0
    # for k in range(1, n + 1):
    #     P += Lagranz(dic, a_new + (k - 1) * h)

    # h = (b - a) / n
    # a_new = a
    # P = 0
    # for k in range(1, n + 1):
    #     P += function(a_new + (k - 1) * h)

    h = (b - a) / n
    P = 0
    for k in range(1, n + 1):
        P += mas[k].a


    return h * P

def rightRectangles(a, b, n, mas, Lagranz):
    # h = (b - a) / n
    # a_new = a + h
    # P = 0
    # for k in range(1, n + 1):
    #     P += Lagranz(dic, a_new + (k - 1) * h)

    # h = (b - a) / n
    # a_new = a + h
    # P = 0
    # for k in range(1, n + 1):
    #     P += function(a_new + (k - 1) * h)

    h = (b - a) / n
    P = 0
    for k in range(1, n + 1):
        P += mas[k].b

    return h * P



def averageRectangles(a, b, n, mas, Lagranz):
    # h = (b - a) / n
    # a_new = a + h / 2
    # P = 0
    # for k in range(1, n + 1):
    #     P += Lagranz(dic, a_new + (k - 1) * h)

    # h = (b - a) / n
    # a_new = a + h / 2
    # P = 0
    # for k in range(1, n + 1):
    #     P += function(a_new + (k - 1) * h)

    h = (b - a) / n
    P = 0
    for k in range(n):
        P += mas[k].w

    return h * P

def trapezoid(a, b, n, mas, Lagranz):
    h = (b - a) / n
    P = 0
    for k in range(0, n + 1):
        if k == 0:
            # P += function(a)
            # P += Lagranz(dic, dic[k].key)
            P += mas[k].a
        elif k == n:
            # P += function(b)
            # P += Lagranz(dic, dic[k].key)
            P += mas[k].a
        else:
            # P += function(a + k * h) * 2
            # P += Lagranz(dic, dic[k].key) * 2
            P += mas[k].a * 2

    return (b - a) / (n * 2) * P

def Simpson(a, b, n, mas, Lagranz):
    h = (b - a) / n
    P = 0
    for k in range(n + 1):
        if k == 0:
            # P += function(a)
            # P += Lagranz(dic, dic[k].key)
            P += mas[k].a
        elif k == n:
            # P += function(b)
            # P += Lagranz(dic, dic[k].key)
            P += mas[k].a
        elif k % 2 == 1:
            # P += function(a + k * h) * 4
            # P += Lagranz(dic, dic[k].key) * 4
            P += mas[k].a * 4
        elif k % 2 == 0:
            # P += function(a + k * h) * 2
            # P += Lagranz(dic, dic[k].key) * 2
            P += mas[k].a * 2

    return (b - a) / (n / 2 * 6) * P

def integrate():
    print("Задача приближённого вычисления интеграла по составным квадратурным формулам.\n")
    a = int(input("Введите левый край отрезка [a, b]: "))
    b = int(input("Введите правый край отрезка [a, b]: "))
    N = int(input("Введите число отрезков разбиения отрезка:"))

    # print("Таблица значений функции и первообразной:")
    mas = separation2(N, a, b)
    masSimpson = separation2(N * 2, a, b)
    # print("%-30s%-30s%-30s" % ("x", "f(x)", "F(x)"))
    # print("%-30s%-30s%-30s" % ("--------", "--------", "--------"))
    # for i in range(len(mas)):
    #     print("%-30s%-30s%-30s" % (mas[i].key, mas[i].value1, mas[i].value2))
    # print("---------------------------------------------\n")

    J = antiderivative(b) - antiderivative(a)
    print(f"\nОпределенный интегралл на промежутке [{a}, {b}] J: ", J, "\n")

    print("Составная квадратурная формула левых прямоугольников:")
    J_h = leftRectangles(a, b, N, mas, Lagranz)
    print("Приближенное значение J(x): ", J_h)
    print("Абсолютная фактическая погрешность |J(x) - J|: ", abs(J - J_h), "\n")

    print("Составная квадратурная формула правых прямоугольников:")
    J_h = rightRectangles(a, b, N, mas, Lagranz)
    print("Приближенное значение J(x): ", J_h)
    print("Абсолютная фактическая погрешность |J(x) - J|: ", abs(J - J_h), "\n")

    print("Составная квадратурная формула средних прямоугольников:")
    J_h = averageRectangles(a, b, N, mas, Lagranz)
    print("Приближенное значение J(x): ", J_h)
    print("Абсолютная фактическая погрешность |J(x) - J|: ", abs(J - J_h), "\n")

    print("Составная квадратурная формула трапеций:")
    J_h = trapezoid(a, b, N, mas, Lagranz)
    print("Приближенное значение J(x): ", J_h)
    print("Абсолютная фактическая погрешность |J(x) - J|: ", abs(J - J_h), "\n")

    print("Составная квадратурная формула Симпсона:")
    J_h = Simpson(a, b, N * 2, masSimpson, Lagranz)
    print("Приближенное значение J(x): ", J_h)
    print("Абсолютная фактическая погрешность |J(x) - J|: ", abs(J - J_h), "\n")

while True:
    integrate()

    repeat = str(input("Хотите продолжить программу? (Да/Нет)"))
    repeat = repeat.lower()
    if repeat == "да":
        print()
    else:
        break