# Выяснить, кратно ли число заданному, если нет, вывести остаток.

a = int(input("Первое число: "))
b = int(input("Второе число: "))
if a % b == 0:
    print('Первое число кратно второму.')
else:
    print("Первое число некратно второму")
    print(f'Остаток от деления {a} на {b} равен {a%b}')
