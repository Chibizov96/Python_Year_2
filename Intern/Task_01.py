# По двум заданным числам проверять является ли первое квадратом второго

a = int(input('A = '))
b = int(input('B = '))
if b*b == a:
    print(f'{a} является квадратом {b}')
elif a*a == b:
    print(f'{b} является квадратом {a}')
else:
    print(f'{a} является квадратом {b}')
