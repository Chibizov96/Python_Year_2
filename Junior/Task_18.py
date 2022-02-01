# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x1 = True
y1 = True
x2 = True
y2 = False
x3 = False
y3 = True
x4 = False
y4 = False


def LogicFunction(x, y):
    result = (not (x or y) == (not x and not y))
    return result


a1 = LogicFunction(x1, y1)
a2 = LogicFunction(x2, y2)
a3 = LogicFunction(x3, y3)
a4 = LogicFunction(x4, y4)

if a1 == a2 == a3 == a4:
    print("Выражение верно")
else:
    print("Выражение неверно")
