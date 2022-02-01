# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
n = random.randint(10, 99)
print(f'{n} - случайно загаданное число')
second_number = n % 10
first_number = (n-second_number)/10
if first_number > second_number:
    print(f'{first_number} - наибольшая цифра в числе')
else:
    print(f'{second_number} - наибольшая цифра в числе')
