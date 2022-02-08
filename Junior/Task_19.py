# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input("Х= "))
y = int(input("Y= "))


def MathSquare(x, y):
    if x == 0 or y == 0:
        return("Координаты не должны быть равны нулю")
    else:
        if x > 0:
            if y > 0:
                return('Четверть 1 ')
            else:
                return('Четверть 4 ')
        else:
            if y > 0:
                return('Четверть 2 ')
            else:
                return('Четверть 3 ')


print(MathSquare(x, y))
