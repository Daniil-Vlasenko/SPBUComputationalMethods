import math


class TebleEl:
    def __init__(self, key, value, firstDerivative, secondDerivative):
        self.key = key
        self.value = value
        self.firstDerivative = firstDerivative
        self.secondDerivative = secondDerivative

def function(x):
    return math.exp(6 * x)
    # return math.pow(x, 3) + 4 * math.pow(x, 2) + 6

def functionFirstDerivative(x):
    return math.exp(6 * x) * 6
    # return 3 * math.pow(x, 2) + 8 * x

def functionSecondDerivative(x):
    return math.exp(6 * x) * 36
    # return 6 * x + 8

def firstDerivative(h, mas):
    for i in range(len(mas)):
        if i == 0:
            mas[i].firstDerivative = (-3 * mas[i].value + 4 * mas[i + 1].value - mas[i + 2].value) / (2 * h)

        elif i == len(mas) -1:
            mas[i].firstDerivative = (3 * mas[i].value - 4 * mas[i - 1].value + mas[i - 2].value) / (2 * h)

        else:
            mas[i].firstDerivative = (mas[i + 1].value - mas[i - 1].value) / (2 * h)

    return mas

def secondDerivative(h, mas):
    for i in range(len(mas)):
        if i != 0 and i != len(mas) - 1:
            mas[i].secondDerivative = (mas[i + 1].value - 2 * mas[i].value + mas[i - 1].value) / (math.pow(h, 2))

    return mas

def makeMas(a, h, m, function):
    mas = []
    count = 0
    for i in range(m):
        mas.append(TebleEl(a + count, function(a + count), None, None))
        count += h

    return mas

def numericalDifferentiation(a, h , m, function):
    mas = makeMas(a, h, m, function)
    mas = firstDerivative(h, mas)
    mas = secondDerivative(h, mas)

    return mas

def printTable(mas):
    print("%-25s%-25s%-25s%-25s%-25s%-25s" % ("x", "f(x)", "f'(x)", "|f'(x)т - f'(x)чд|", 'f"(x)', '|f"(x)т - f"(x)чд|'))
    print("%-25s%-25s%-25s%-25s%-25s%-25s" % ("--------", "--------","--------","--------","--------","--------"))
    for i in range(len(mas)):
        if i == 0 or i == len(mas) -1:
            print("%-25s%-25s%-25s%-25s" % (mas[i].key, mas[i].value, mas[i].firstDerivative, abs(mas[i].firstDerivative - functionFirstDerivative(mas[i].key))))

        else:
            print("%-25s%-25s%-25s%-25s%-25s%-25s" % (mas[i].key, mas[i].value, mas[i].firstDerivative, abs(mas[i].firstDerivative - functionFirstDerivative(mas[i].key)), mas[i].secondDerivative, abs(mas[i].secondDerivative - functionSecondDerivative(mas[i].key))))
    print()

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def main():
    print("Задача нахождения производных таблично-заданной функции по формулам численного дифференцирования")
    print("f(x) = exp(6x)")
    a = float(input("Ведите первый узел разбиения a: "))
    h = float(input("Ведите шаг разбиения h: "))
    m = int(input("Ведите число узлов разбияния m: "))
    mas = numericalDifferentiation(a, h, m, function)
    printTable(mas)

main()