# Задать номер четверти, вывести диапазоны координат

from ast import Return
import re


n = int(input("Номер четверти = "))


def Coord(n):
    if n == 1:
        return("x>0, y>0")
    elif n == 2:
        return("x<0, y>0")
    elif n == 3:
        return("x<0, y<0")
    elif n == 4:
        return("x>0, y<0")
    else:
        return("Такой плоскости нет, введите число от 1 до 4")


print(Coord(n))
