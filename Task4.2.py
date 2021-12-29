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

def p(x):
    return 1

class Section:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

def separation(m, a, b):
    mas = []
    h = (b - a) / m
    for i in range(m + 1):
        af = function(a + i * h) * p(a + i * h)
        bf = function(a + (i + 1) * h) * p(a + (i + 1) * h)
        wf = function(a + i * h + h / 2) * p(a + i * h + h / 2)

        mas.append(Section(af, bf, wf))

    return mas

def leftRectangles(a, b, n, mas):
    h = (b - a) / n
    P = 0
    for k in range(1, n + 1):
        P += mas[k].a


    return h * P

def rightRectangles(a, b, n, mas):
    h = (b - a) / n
    P = 0
    for k in range(1, n + 1):
        P += mas[k].b

    return h * P

def averageRectangles(a, b, n, mas):
    h = (b - a) / n
    P = 0
    for k in range(n):
        P += mas[k].w

    return h * P

def trapezoid(a, b, n, mas):
    h = (b - a) / n
    P = 0
    for k in range(0, n + 1):
        if k == 0:
            P += mas[k].a
        elif k == n:
            P += mas[k].a
        else:
            P += mas[k].a * 2

    return (b - a) / (n * 2) * P

def Simpson(a, b, n, mas):
    h = (b - a) / n
    P = 0
    for k in range(n + 1):
        if k == 0:
            P += mas[k].a
        elif k == n:
            P += mas[k].a
        elif k % 2 == 1:
            P += mas[k].a * 4
        elif k % 2 == 0:
            P += mas[k].a * 2

    return (b - a) / (n / 2 * 6) * P

def integrate():
    print("Задача приближённого вычисления интеграла по составным квадратурным формулам.\n")
    a = int(input("Введите левый край отрезка [a, b]: "))
    b = int(input("Введите правый край отрезка [a, b]: "))
    N = int(input("Введите число отрезков разбиения отрезка: "))
    l = int(input("Введите парамет увеличения числа отрезков разбиения, l: "))

    mas = separation(N, a, b)
    masl = separation(N * l, a, b)
    masSimpson = separation(N * 2, a, b)
    masSimpsonl = separation(N * l * 2, a, b)

    J = antiderivative(b) - antiderivative(a)
    print(f"\nОпределенный интегралл на промежутке [{a}, {b}] J: ", J, "\n")

    print("Составная квадратурная формула левых прямоугольников:")
    J_h = leftRectangles(a, b, N, mas)
    J_hl = leftRectangles(a, b, N * l, masl)
    J_R = J_hl + (J_h - J_hl)/(1 - math.pow(l, 1))
    print("Приближенное значение J(h): ", J_h)
    print("Приближенное значение J(h/l): ", J_hl)
    print("Приближенное значение J_R: ", J_R)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))
    print("Абсолютная фактическая погрешность |J(h/l) - J|: ", abs(J - J_hl))
    print("Абсолютная фактическая погрешность |J_R - J|: ", abs(J - J_R), "\n")

    print("Составная квадратурная формула правых прямоугольников:")
    J_h = rightRectangles(a, b, N, mas)
    J_hl = rightRectangles(a, b, N * l, masl)
    J_R = J_hl + (J_h - J_hl) / (1 - math.pow(l, 1))
    print("Приближенное значение J(h): ", J_h)
    print("Приближенное значение J(h/l): ", J_hl)
    print("Приближенное значение J_R: ", J_R)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))
    print("Абсолютная фактическая погрешность |J(h/l) - J|: ", abs(J - J_hl))
    print("Абсолютная фактическая погрешность |J_R - J|: ", abs(J - J_R), "\n")

    print("Составная квадратурная формула средних прямоугольников:")
    J_h = averageRectangles(a, b, N, mas)
    J_hl = averageRectangles(a, b, N * l, masl)
    J_R = J_hl + (J_h - J_hl) / (1 - math.pow(l, 2))
    print("Приближенное значение J(h): ", J_h)
    print("Приближенное значение J(h/l): ", J_hl)
    print("Приближенное значение J_R: ", J_R)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))
    print("Абсолютная фактическая погрешность |J(h/l) - J|: ", abs(J - J_hl))
    print("Абсолютная фактическая погрешность |J_R - J|: ", abs(J - J_R), "\n")

    print("Составная квадратурная формула трапеций:")
    J_h = trapezoid(a, b, N, mas)
    J_hl = trapezoid(a, b, N * l, masl)
    J_R = J_hl + (J_h - J_hl) / (1 - math.pow(l, 2))
    print("Приближенное значение J(h): ", J_h)
    print("Приближенное значение J(h/l): ", J_hl)
    print("Приближенное значение J_R: ", J_R)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))
    print("Абсолютная фактическая погрешность |J(h/l) - J|: ", abs(J - J_hl))
    print("Абсолютная фактическая погрешность |J_R - J|: ", abs(J - J_R), "\n")

    print("Составная квадратурная формула Симпсона:")
    J_h = Simpson(a, b, N * 2, masSimpson)
    J_hl = Simpson(a, b, N * l * 2, masSimpsonl)
    J_R = J_hl + (J_h - J_hl) / (1 - math.pow(l, 4))
    print("Приближенное значение J(h): ", J_h)
    print("Приближенное значение J(h/l): ", J_hl)
    print("Приближенное значение J_R: ", J_R)
    print("Абсолютная фактическая погрешность |J(h) - J|: ", abs(J - J_h))
    print("Абсолютная фактическая погрешность |J(h/l) - J|: ", abs(J - J_hl))
    print("Абсолютная фактическая погрешность |J_R - J|: ", abs(J - J_R), "\n")

while True:
    integrate()

    repeat = str(input("Хотите продолжить программу? (Да/Нет)"))
    repeat = repeat.lower()
    if repeat == "да":
        print()
    else:
        break