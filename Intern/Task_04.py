# По заданному номеру дня недели вывести его название
dayNum = int(input('Введите номер дня: '))
if dayNum == 1:
    print('Это понедельник')
elif dayNum == 2:
    print('Это вторник')
elif dayNum == 3:
    print('Это среда')
elif dayNum == 4:
    print('Это четверг')
elif dayNum == 5:
    print('Это пятница')
elif dayNum == 6:
    print('Это суббота')
elif dayNum == 7:
    print('Это воскресенье')
else:
    print('Нет такого дня недели')
