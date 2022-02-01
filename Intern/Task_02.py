# Даны два числа. Показать большее и меньшее число
a = int(input('A = '))
b = int(input('B = '))
if a != b:
    print(f'Большее {max(a, b)}, меньшее {min(a, b)}')
else:
    print(f'Числа равны')
