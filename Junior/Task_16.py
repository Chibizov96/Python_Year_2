# Дано число обозначающее день недели. Выяснить является номер дня недели выходным
a = int(input("Введите число дня недели: "))


def DayOfWeek(a):
    if a < 6 and a > 0:
        return("Не выходой :(")
    elif a > 5 and a < 8:
        return("Выходной :)")
    else:
        return("Неверное число")


print(DayOfWeek(a))
