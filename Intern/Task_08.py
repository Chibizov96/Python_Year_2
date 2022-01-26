# Показать числа от -N до N
n = int(input("N = "))
print(f'Числа от -{n} до {n}')
for i in range(n*-1, n+1):
    print(i, end=" ")
