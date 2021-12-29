import math
from prettytable import PrettyTable



def functionF(x, y):
    return -2 * y + math.pow(y, 2)
    # return 1

def functionY(x):
    return 2 / (math.exp(2 * x) + 1)
    # return x

class realY:
    def __init__(self, N, h, x0, y0):
        self.N = N
        self.h = h

        masx, masy = [x0], [y0]
        for k in range(1, N):
            masx.append(x0 + k * h)
            masy.append(functionY(x0 + k * h))

        self.masx = masx
        self.masy = masy

def Euler1(N, h, masx, y0):
    masy = [y0]
    for m in range(1, N):
        masy.append(masy[m - 1] + h * functionF(masx[m - 1], masy[m - 1]))

    return masy

def Euler2(N, h, masx, y0):
    masy = [y0]
    for m in range(1, N):
        x = masx[m - 1] + h / 2
        y = masy[m - 1] + h / 2 * functionF(masx[m - 1], masy[m - 1])
        masy.append(masy[m - 1] + h * functionF(x, y))

    return masy

def Euler3(N, h, masx, y0):
    masy = [y0]
    for m in range(1, N):
        y = masy[m - 1] + h * functionF(masx[m - 1], masy[m - 1])
        masy.append(masy[m - 1] + h / 2 * (functionF(masx[m - 1], masy[m - 1]) + functionF(masx[m], y)))

    return masy

def Runge(N, h, masx, y0):
    masy = [y0]
    for m in range(1, N):
        k1 = h * functionF(masx[m - 1], masy[m - 1])
        k2 = h * functionF(masx[m - 1] + h / 2, masy[m - 1] + k1 / 2)
        k3 = h * functionF(masx[m - 1] + h / 2, masy[m - 1] + k2 / 2)
        k4 = h * functionF(masx[m - 1] + h, masy[m - 1] + k3)
        masy.append(masy[m - 1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

    return masy

def Adams(N, h, masx, masy):
    masq, masd1q, masd2q, masd3q, masd4q = [], [], [], [], []

    for i in range(5):
        masq.append(h * functionF(masx[i], masy[i]))
    for i in range(4):
        masd1q.append((masq[i + 1] - masq[i]))
    for i in range(3):
        masd2q.append((masd1q[i + 1] - masd1q[i]))
    for i in range(2):
        masd3q.append((masd2q[i + 1] - masd2q[i]))
    for i in range(1):
        masd4q.append((masd3q[i + 1] - masd3q[i]))

    masy.append(masy[-1] + masq[-1] + 1 / 2 * masd1q[-1] + 5 / 12 * masd2q[-1] + 3 / 8 * masd3q[-1] + 251 / 720 * masd4q[-1])

    for i in range(5, N - 1):
        masq.append(h * functionF(masx[i], masy[i]))
        masd1q.append((masq[i] - masq[i - 1]))
        masd2q.append((masd1q[-1] - masd1q[-2]))
        masd3q.append((masd2q[-1] - masd2q[-2]))
        masd4q.append((masd3q[-1] - masd3q[-2]))

        masy.append(
            masy[-1] + masq[-1] + 1 / 2 * masd1q[-1] + 5 / 12 * masd2q[-1] + 3 / 8 * masd3q[-1] + 251 / 720 * masd4q[
                -1])

    return masy


print('Численное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка\n')
x0 = 0
y0 = 1
N = int(input('Введите параметр N: ')) + 1
h = float(input('Введите параметр h: '))

realValue = realY(N, h, x0, y0)

masy1 = Euler1(N, h, realValue.masx, y0)
print('\nПервый метод Эйлера.')
pretty_table = PrettyTable(['x', 'y', 'yk - y(xk)'])
for i in range(N):
    pretty_table.add_row([realValue.masx[i], masy1[i], math.fabs(masy1[i] - realValue.masy[i])])
print(pretty_table)

masy2 = Euler2(N, h, realValue.masx, y0)
print('\nВторой метод Эйлера.')
pretty_table = PrettyTable(['x', 'y', 'yk - y(xk)'])
for i in range(N):
    pretty_table.add_row([realValue.masx[i], masy2[i], math.fabs(masy2[i] - realValue.masy[i])])
print(pretty_table)

masy3 = Euler3(N, h, realValue.masx, y0)
print('\nТретий метод Эйлера.')
pretty_table = PrettyTable(['x', 'y', 'yk - y(xk)'])
for i in range(N):
    pretty_table.add_row([realValue.masx[i], masy3[i], math.fabs(masy3[i] - realValue.masy[i])])
print(pretty_table)

masy4 = Runge(N, h, realValue.masx, y0)
print('\nМетод Рунге-Кутта.')
pretty_table = PrettyTable(['x', 'y', 'yk - y(xk)'])
for i in range(N):
    pretty_table.add_row([realValue.masx[i], masy4[i], math.fabs(masy4[i] - realValue.masy[i])])
print(pretty_table)

masy = realValue.masy[0: 5]
masy5 = Adams(N, h, realValue.masx, masy)
print('\nМетод Адамса 4-го порядка.')
pretty_table = PrettyTable(['x', 'y', 'yk - y(xk)'])
for i in range(N):
    pretty_table.add_row([realValue.masx[i], masy5[i], math.fabs(masy5[i] - realValue.masy[i])])
print(pretty_table)


print('\n\nПогрешности для y(x(N)):')
pretty_table = PrettyTable(['Первый метод Эйлера', 'Второй метод Эйлера', 'Третий метод Эйлера', 'Метод Рунге-Кутта', 'Метод Адамса'])
pretty_table.add_row([math.fabs(masy1[-1] - realValue.masy[-1]), math.fabs(masy2[-1] - realValue.masy[-1]), math.fabs(masy3[-1] - realValue.masy[-1]), math.fabs(masy4[-1] - realValue.masy[-1]), math.fabs(masy5[-1] - realValue.masy[-1])])
print()
print(pretty_table)